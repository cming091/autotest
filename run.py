# coding=utf-8
import pytest
import sys
import getopt
import logging
import time
import os
import argparse
from utils import cfg
from lib.logs import LogConfig
from lib.rd_platform import RdPlatform


if __name__ == "__main__":
    runtime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    report_path = os.sep.join(['report', runtime])

    if len(sys.argv) < 2:
        print("usage: python3 run.py -c case_path1 case_path2 ...")
        exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument('--cases', '-c', nargs='+', help='测试用例路径, 多个用例之间用逗号分隔')
    parser.add_argument('--options', help='params from cmd')
    parser.add_argument('--cluster', action='store_true', help='cluster mode')
    parser.add_argument('--exitfirst', '-x', action='store_true', help='exit when first fail')
    parser.add_argument('--update_service_version', action='store_true', help='update service by api of rd platform')
    parser.add_argument('--coverage', action='store_true', help='coverage test mode')
    parser.add_argument('--collectTestCase', help='collect test case')
    parser.add_argument('--mode', help='run mode')
    parser.add_argument('--alluredir', help='allure report dir')
    parser_args = parser.parse_args()

    mode = parser_args.mode
    options = parser_args.options
    cluster = parser_args.cluster
    exitfirst = parser_args.exitfirst
    coverage = parser_args.coverage
    cases = parser_args.cases
    allure_dir = parser_args.alluredir
    collectTestCaseDir = parser_args.collectTestCase
    update_service_version = parser_args.update_service_version

    root_path = os.path.dirname(os.path.realpath(__file__))
    cf_path = os.path.join(root_path, './conf/config.ini')
    cfg.load_cfg(cf_path, options, mode)

    if update_service_version:
        service_name = cfg.G_CONFIG_DICT['coverage.service_name']
        logging.info(f'update service {service_name}')
        version = cfg.G_CONFIG_DICT['version_with_coverage']
        logging.info(f'version: {version}')
        rdp = RdPlatform()
        res = rdp.update_service(service_name, version)
        sys.exit(0 if res == 'succ' else 1)

    if allure_dir:
        report_path = allure_dir

    log_format = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    log_date_format = '%Y-%m-%d %H:%M:%S'

    args = ["-s", "-v", "--cache-clear", "--log-format=%s" % log_format, "--log-date-format=%s" % log_date_format, "--alluredir=%s" % report_path, "-Wignore"]
    if exitfirst:
        args.append("-x")

    if cluster:
        args.append("--cluster")
    if not collectTestCaseDir:
        for case in cases:
            args.append(case)
    else:
        args = ["--collectTestCase", "-Wignore", collectTestCaseDir]
    print(args)

    LogConfig()
    ret = pytest.main(args)
    if not options:
        print(f'to generate report, run: allure generate -c {report_path}')
        print('to open report in explorer, run: allure open')
    if ret == 0 or ret == 1:
        os.system(f"allure generate -c {report_path}")

    # 区分正常测试模式和覆盖率测试模式，覆盖率测试需要在这里杀进程和取覆盖率文件
    if coverage:
        service_name = cfg.G_CONFIG_DICT['coverage.service_name']
        logging.info(f'kill service {service_name}')
        # 对于service_name的存在性检查，放在HTP平台上
        rdp = RdPlatform()
        res = rdp.kill_service('target.COV', service_name)
        logging.info(f'kill service {service_name}: {ret}')

        time.sleep(5)
        res = rdp.get_file_from_docker(service_name)
        logging.info(f'get coverage file of service {service_name} from docker: {res}')
    print("after all, ret = ", ret)
    sys.exit(ret)
