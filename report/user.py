from tc_case.requetes import Request
from confdb.Tim_Api import *

class Api():
    """
    存放用例的调用接口方法
    """
    def __init__(self):
        self.Requests=Request()

    def Get(self,api,dict_requet={}):
        return self.Requests.Get(api,dict_requet)

    def Post(self,api,dict_requet={}):
        return self.Requests.Post(api,dict_requet)

    def Put(self,api,dict_requet={}):
        return self.Requests.Put(api,dict_requet)

    def Delete(self,api,dict_requet={}):
        return self.Requests.Delete(api,dict_requet)

    def weather(self,dict_ruster={}):
        """
        获取客户信息
        :return:
        """
        dict={
            "keywords":"",
        }
        dict.update(dict_ruster)
        reponses=self.Get(Tim_api_get_apone,dict)
        if reponses["ret"]==0:
            b_ret=True
        else:
            b_ret=False
        return b_ret

    def login(self,dict_ruster={}):
        """
                登录接口
                :return:
                """
        dict = {
            "username": "byhy",
            "password": "88888888"
        }
        dict.update(dict_ruster)#将传进来的参数更新到dict,已有的参数会更新，没有则新增
        reponses = self.Post(Tim_api_login_byhy,dict)#第一个参数是接口模板，第二个是你要传输的接口参数信息。第三个是一个预留的传参位
        if reponses["ret"] == 0:
            b_ret = True
        else:
            b_ret = False
        return b_ret,reponses

    def Create(self,dict_ruster={}):
        """
        创建用户
        :param dict_ruster:
        :return:
        """
        reponses = self.Post(Tim_api_create_User,dict_ruster)
        if reponses["ret"] == 0:
            b_ret = True
        else:
            b_ret = False
        return b_ret,reponses

