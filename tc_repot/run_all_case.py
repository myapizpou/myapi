import unittest
import os
from commenlib import HTMLTestRunner
from datetime import *


def all_case():
    """
    生成测试报告于case_report
    :return:
    """
    now = datetime.now()
    timestr = now.strftime("%Y_%m_%d_%H_%M_%S")
    result_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
    html = f'\\case_report\\report_{timestr}.html'
    fb = open(result_path+html, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title="测试报告",
        description="自动化测试用例执行情况"
    )
    case_dir=os.path.abspath(os.path.join(os.getcwd(), ".."))+'\\case'
    discover=unittest.defaultTestLoader.discover(
        case_dir,
        pattern='test*.py'
    )
    runner.run(discover)
    fb.close()


if __name__ == '__main__':
    all_case()
