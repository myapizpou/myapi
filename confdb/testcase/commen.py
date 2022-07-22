from confdb.flow import *
from commenlib.flow.commen_sql import FlowText
from commenlib.syetem.mcom import *


class Integrate(FlowClient):
    def __init__(self):
        # log
        self.Clog = CLOGS()
        # sql连接
        self.sql = FlowText()
        # 文件处理
        self.file = Mfile()
        # flow集成
        FlowClient.__init__(self)

    def base_assert(self, message, actual, exception=True):
        """
        断言
        :return:
        """
        if actual == exception:
            self.Clog.info(f'b_ret value: {message},{actual}')
        else:
            self.Clog.info(f'b_ret value: {message},{actual}')
            self.file.error_step()
            raise Exception("Use case execution failed")

    def base_step(self, str_step):
        """
        打印执行步骤
        :param str_step:
        :return:
        """
        return CCom().base_step(str_step)
