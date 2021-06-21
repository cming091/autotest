# coding=utf-8
from utils import cfg
import logging
import time
import os


class LogFilter(logging.Filter):
    def __init__(self, level):
        super().__init__()
        self.level = level

    def filter(self, record: logging.LogRecord) -> int:
        return record.levelno < self.level


class LogConfig:
    def __init__(self):
        """
        日志配置
        """
        runtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        logs_dir = os.path.dirname(os.path.dirname(__file__)) + "/" + cfg.G_CONFIG_DICT['base.log_path']
        if os.path.exists(logs_dir):
            print('logs_dir is', logs_dir)
        else:
            try:
                os.makedirs(logs_dir)
            except OSError as e:
                print(f'make logs dir error, {e}')
                exit(1)

        logfile = cfg.G_CONFIG_DICT['base.log_path'] + "/" + "log-" + runtime + '.log'
        fh = logging.FileHandler(logfile, 'a')
        fh.setLevel(logging.DEBUG)
        fh_filter = LogFilter(logging.ERROR)
        fh.addFilter(fh_filter)

        logfile_error = cfg.G_CONFIG_DICT['base.log_path'] + "/" + "log-" + runtime + '_error.log'
        fh_error = logging.FileHandler(logfile_error, 'a')
        fh_error.setLevel(logging.ERROR)

        console = logging.StreamHandler()
        # console.setLevel(logging.DEBUG)

        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        fh_error.setFormatter(formatter)
        console.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(fh_error)
        logger.addHandler(console)
