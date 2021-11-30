from report.user import Api
from commen.Tcose import TestCase
import unittest

class Login(TestCase):
    """
    地址改了，咱不能用
    """
    def setUp(self):
        self.name("zpou") #用例编写人
        self.user=Api() #实例化
        self.step = 1 #初始化步骤

    def test_run(self):
        bart_step="first"
        self.show(bart_step)
        dict_login = {
            "action": "list_customer",
            "pagenum": "1",
            "pagesize":"5",
            "keywords":"",
            "_":"1636857714680"
        }
        b_ret=self.user.weather(dict_login)
        if not b_ret:
            raise("login fail")
        bart_step = "last"
        self.show(bart_step)

if __name__ == '__main__':
    unittest.main()