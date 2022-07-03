from confdb.flow import *


class COS(FlowClient):
    """
    基础flow层的类，方便testcase层调用，上下按格式添加
    """

    def __init__(self):
        FlowClient.__init__(self)
