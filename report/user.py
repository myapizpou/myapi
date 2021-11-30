from tc_case.requetes import Request
from confdb.Tim_Api import *

class Api():
    """
    存放用例的调用接口方法
    """
    def __init__(self):
        self.Requests=Request()
        #登录所用的账号，如果要换账号保持登录态，请在方法内更新这个账号密码
        self.dict_rester={
            "username": "byhy",
            "password": "88888888"
        }

    def Get(self,api,dict_requet={},dict_rester={}):
        return self.Requests.Get(api,dict_requet,dict_rester)

    def Post(self,api,dict_requet={},dict_rester={}):
        return self.Requests.Post(api,dict_requet,dict_rester)

    def Put(self,api,dict_requet={},dict_rester={}):
        return self.Requests.Put(api,dict_requet,dict_rester)

    def Delete(self,api,dict_requet={},dict_rester={}):
        return self.Requests.Delete(api,dict_requet,dict_rester)

    def weather(self,dict_ruster={}):
        """
        获取客户信息
        :return:
        """
        dict={
            "keywords":"",
        }
        dict.update(dict_ruster)
        reponses=self.Get(Tim_api_get_apone,dict,self.dict_rester)
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
        dict.update(dict_ruster)
        reponses = self.Post(Tim_api_login_byhy,dict,self.dict_rester)
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
        reponses = self.Post(Tim_api_create_User,dict_ruster,self.dict_rester)
        if reponses["ret"] == 0:
            b_ret = True
        else:
            b_ret = False
        return b_ret,reponses

