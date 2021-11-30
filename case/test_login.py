from report.user import Api
from commen.Tcose import TestCase
import unittest

class Login(TestCase):
    def setUp(self):
        self.name("zpou") #执行人
        self.user=Api() #实例化
        self.step = 1 #初始化步骤

    def test_run(self):
        bart_step="first login"
        self.show(bart_step)
        dict_login = {
            "username": "byhy",
            "password": "88888888"
        }
        b_ret,reponses=self.user.login(dict_login)
        if not b_ret:
            raise print("login failed")
        bart_step = "last"
        self.show(bart_step)

    def test_ceate(self):
        bart_step = "create client"
        self.show(bart_step)
        dict = {
            "action": "add_customer",
            "data": {
                "name": "fsad",
                "phonenumber": "1254654666",
                "address": "635356"
            }
        }
        b_ret,reponses = self.user.Create(dict)
        if not b_ret:
            raise ("create fail")

if __name__ == '__main__':
    unittest.main()