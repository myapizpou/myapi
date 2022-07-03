from confdb.flow import *


class Integrate(FlowClient):
    def __init__(self):
        # log
        self.Clog = CLOGS()
        # flow集成
        FlowClient.__init__(self)

    def base_assert(self, message, actual=True):
        """
        断言
        :return:
        """
        if actual:
            self.Clog.info(f'b_ret value: {actual},{message}')
        else:
            self.Clog.error(f'b_ret value: {actual},{message}')
            raise Exception("Use case execution failed")
