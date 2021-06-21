# coding=utf-8
import logging
import paramiko
from paramiko import AuthenticationException, BadHostKeyException, SSHException
from paramiko.client import SSHClient, AutoAddPolicy
from paramiko.ssh_exception import NoValidConnectionsError

from lib.rd_platform import RdPlatform
from utils import cfg
import os


class Shell:
    def __init__(self):
        self.ssh_client = SSHClient()

    def ssh_login(self, log_server=False, use_password=False):
        if log_server:
            username = cfg.G_CONFIG_DICT['ssh.log_path']
        else:
            username = cfg.G_CONFIG_DICT['ssh.username']
        root_path = os.path.dirname(os.path.dirname(__file__))
        key = cfg.G_CONFIG_DICT['ssh.key']
        private_key = paramiko.RSAKey.from_private_key_file(root_path + '/' + key)
        try:
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            if use_password:
                password = cfg.G_CONFIG_DICT['ssh.password']

                self.ssh_client.connect(cfg.G_CONFIG_DICT['base.url_base'].split('//')[1], port=cfg.G_CONFIG_DICT['ssh.port'], username=username, password=password)
            else:
                self.ssh_client.connect(cfg.G_CONFIG_DICT['base.url_base'].split('//')[1], port=cfg.G_CONFIG_DICT['ssh.port'], username=username, pkey=private_key)
        except BadHostKeyException as e:
            logging.error("ssh login, something wrong with host key! ", e)
            exit(1)
        except AuthenticationException as e:
            logging.error("ssh login, username or password error! ", e)
            exit(1)
        except NoValidConnectionsError as e:
            logging.error("ssh login, connect time out! ", e)
            exit(1)
        except SSHException as e:
            logging.error("ssh login, ssh exception occured!", e)
            exit(1)
        except Exception as e:
            logging.error("ssh login, unknown error! ", e)
            exit(1)

    def exec_command(self, command):
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        return stdout.read().decode()

    def restart(self, name):
        command = "docker ps | grep %s | awk '{print $1}'" % name
        logging.debug("find image %s, command is %s" % (name, command))
        image_id = self.exec_command(command)
        if image_id == "":
            logging.error("can not find %s in docker, image id is null" % name)
            exit(1)
        elif not image_id.strip().isalnum():
            logging.error("image id is invalid: %s" % image_id)
            exit(1)

        command = "docker restart %s" % image_id
        logging.debug("restart image %s, image_id is %s, command is %s" % (name, image_id, command))
        image_id_restart = self.exec_command(command)
        if image_id_restart != image_id:
            logging.error("restart %s fail, %s" % image_id_restart)
            exit(1)
        logging.debug("restart image %s ok!" % name)

    def open_sftp(self):
        return self.ssh_client.open_sftp()

    def ssh_logout(self):
        logging.debug("ssh logout")
        self.ssh_client.close()


# if __name__ == '__main__':
#     import os
#
#     root_path = os.path.dirname(os.path.dirname(__file__))
#     print('root_path: ', root_path)
#     cfg_path = os.path.join(root_path, './conf/config.ini')
#     cfg.load_cfg(cfg_path)
#
#     # print("当前目录为：", os.getcwd())
#     # os.chdir("../")
#     # print("当前目录为：", os.getcwd())
#     shell = Shell()
#     shell.ssh_login()
#     res = shell.exec_command('ls -l /')
#     print("res: ", res)
