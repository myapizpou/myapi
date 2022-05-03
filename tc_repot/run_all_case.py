import os,unittest
import time
import os
from datetime import datetime
from commen import HTMLTestRunner
from datetime import *
from Public_variable.variable import *

def all_case():
    """
    生成测试报告于case_report
    :return:
    """
    now = datetime.now()  # 获得当前时间
    timestr = now.strftime("%Y_%m_%d_%H_%M_%S")
    result_path = os.path.abspath(os.path.join(os.getcwd(), ".."))#生成测试报告的目录
    html=f'\\case_report\\report_{timestr}.html'
    fb = open(result_path+html, "wb")#打开测试报告的html文件
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title="测试报告",#测试报告的标题
        description="自动化测试用例执行情况"#描述
    )
    case_dir=os.path.abspath(os.path.join(os.getcwd(), ".."))+'\\case'#获取case的路径，即要执行的用例目录
    discover=unittest.defaultTestLoader.discover(
        case_dir,#需要执行的用例文件地址
        pattern='test*.py'#case目录下所有test开头的py文件
    )
    runner.run(discover)#生成测试报告
    fb.close()#关闭文件

if __name__=='__main__':
    all_case()