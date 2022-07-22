from commenlib.mysql_api import Usql
from commenlib.checklib import *


class CSQLtest(Usql):

    def __init__(self):
        # 校验处理数据
        self.check = Check()
        Usql.__init__(self)

