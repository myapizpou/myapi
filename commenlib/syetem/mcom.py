from Public_variable.clog import *
from commenlib.syetem.mfile import *
import warnings
import time


class CCom(object):

    def __init__(self):
        self.Clog = CLOGS()
        self.file = Mfile()
        warnings.simplefilter("ignore", ResourceWarning)

    def base_step(self, str_step):
        """
        打印执行步骤
        :param str_step:
        :return:
        """
        time.sleep(1)
        self.Clog.info(f'步骤{self.file.open_file()}: {str_step}')

    def base_last_step(self):
        """
        打印执行最后步骤
        :param str_step:
        :return:
        """
        self.file.count_step()

