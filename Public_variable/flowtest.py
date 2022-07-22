from confdb.api import *
from Public_variable.clog import *
from commenlib.syetem.mjson import *


class CNSflowtest(ApiUser,
                  ApiClient):
    """
    每在api层增加一个class，就需要在这里继承userapi,下面按格式编写
    """

    def __init__(self):
        # log
        self.Clog = CLOGS()
        # json处理脚本
        self.mjson = Mjson()
        # 集成接口
        ApiUser.__init__(self)
        ApiClient.__init__(self)
        pass
