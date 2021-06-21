import logging
from lib.rd_platform import RdPlatform
from utils import cfg
from utils.shell import Shell
import os
import subprocess
import io
import sys


def run_shell_cmd(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
    proc.wait()
    stream_stdout = io.TextIOWrapper(proc.stdout, encoding='utf-8')
    stream_stderr = io.TextIOWrapper(proc.stderr, encoding='utf-8')

    str_stdout = str(stream_stdout.read())
    str_stderr = str(stream_stderr.read())

    return str_stdout, str_stderr


def update_config(service_name, tpl_path, replace_dict):
    """更新服务器端的配置文件"""
    logging.debug(f'update config, service_name={service_name}, tpl_path={tpl_path}, replace_dict={replace_dict}')
    cfg_file_name = os.path.basename(tpl_path)
    shell = Shell()
    shell.ssh_login()

    # 1.获取环境中service的version
    rdp = RdPlatform()
    version = rdp.get_service_version(service_name)
    logging.debug(f'get version of service {service_name}: {version}')

    # 2.拼装配置文件的完整路径
    full_cfg_path = '/data/srg/' + service_name + '/' + version + '/conf'
    logging.debug(f'full path of config file: {full_cfg_path}')

    # 3.读取本地的配置文件，并替换
    new_cfg_str = ''
    with open(tpl_path) as f:
        for line in f:
            sharp_index = line.find('#')
            if sharp_index != -1:
                line = line.replace(line[sharp_index:-1], '')

            for key in replace_dict:
                v = '{' + key + '}'
                if v in line:
                    line = line.replace(v, replace_dict[key])
            new_cfg_str += line

    # 4.备份旧的配置文件
    command = 'cd ' + full_cfg_path + ';cp ' + cfg_file_name + ' ' + cfg_file_name + '.bak'
    shell.exec_command(command)

    # 5.写入新的配置文件
    ftp = shell.open_sftp()
    file = ftp.file(full_cfg_path + '/' + cfg_file_name, "w")
    file.write(new_cfg_str)
    file.flush()
    ftp.close()
    shell.ssh_logout()


# def clone_from_git(repo, branch):
#     return os.system(f'git clone {repo} -b {branch}')
#
#
# def find_grpc_proto_dirs(path):
#     """在lib目录下搜索grpc的.proto文件，返回路径列表"""
#     file_names = os.listdir(path)
#     res = []
#
#     for file in file_names:
#         sub_path = path + os.sep + file
#         # sub_path = path
#         if os.path.isdir(sub_path):
#             res += find_grpc_proto_dirs(sub_path)
#         else:
#             if file.endswith('.proto'):
#                 res.append(path)
#                 break
#     return res
#
#
# def compile_grpc_protos(grpc_path, proto_list):
#     """
#     编译grpc，生成python代码
#     python3 -m grpc_tools.protoc  --python_out=lib/grpc/processflowengine/pfe-grpc/src/main/proto --grpc_python_out=lib/grpc/processflowengine/pfe-grpc/src/main/proto -Ilib/grpc/processflowengine/pfe-grpc/src/main/proto ./lib/grpc/processflowengine/pfe-grpc/src/main/proto/common/*.proto
#     """
#     for proto_file in proto_list:
#         cmd = f'python3 -m grpc_tools.protoc --proto_path={grpc_path}  --python_out={grpc_path} --grpc_python_out={grpc_path} {proto_file}/*.proto'
#         ret = os.system(cmd)
#         print('cmd: ', cmd, ', ret: ', ret)


# if __name__ == '__main__':
#     root_path = os.path.dirname(os.path.dirname(__file__))
#     print('root_path: ', root_path)
#     cfg_path = os.path.join(root_path, './conf/config.ini')
#     cfg.load_cfg(cfg_path)
#
#     repo = cfg.G_CONFIG_DICT['frworkstation.repo']
#     branch = cfg.G_CONFIG_DICT['frworkstation.branch']
#     ret = clone_from_git(repo, branch)
#     if ret != 0:
#         logging.error(f'clone from git error! repo: {repo}, branch: {branch}')
#
#     grpc_path = cfg.G_CONFIG_DICT['frworkstation.grpc_path']
#     curr_path = os.getcwd()
#     print(curr_path + '/' + grpc_path)
#     proto_list = find_grpc_proto_dirs(curr_path + '/' + grpc_path)
#     print(proto_list)
#
#     compile_grpc_protos(grpc_path, proto_list)

    # proto_list = find_grpc_protos(root_path + '/lib/grpc')
    # print(proto_list)
    # compile_grpc_protos(root_path, proto_list)
#
#     # 更新服务器端的配置文件
#     service_name = 'sim-conveyor'
#     tpl_path = os.path.join(root_path, 'utils/conveyor_630_bak.yaml')
#     replace_dict = {'warehouseID': '1234567890'}
#     update_config(service_name, tpl_path, replace_dict)
#
#     # 执行shell
#     cmd = 'mysql -h 10.170.124.47 -uroot -p1234567890/// < /Users/zhangjinqiang/Downloads/flipagv_sql_715_env.sql'
#     str_stdout, str_stderr = run_shell_cmd(cmd)
#     print('str_stdout: ', str_stdout)
#     print('str_stderr: ', str_stderr)
#     if 'ERROR' in str_stdout or 'ERROR' in str_stderr:
#         print('there are some errors while running shell command')
#
