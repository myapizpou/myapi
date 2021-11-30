import os,unittest
import time
from commen import HTMLTestRunner

def all_case():
    """
    生成测试报告于case_report
    :return:
    """
    Time=time.strftime("%Y%m%d_%H%M%S", time.localtime())
    result_path = os.path.abspath(os.path.join(os.getcwd(), ".."))#生成测试报告的目录
    html=f'\\case_report\\report_{Time}.html'
    print(result_path+html)
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
    #返回实例
    all_case()