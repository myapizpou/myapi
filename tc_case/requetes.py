import requests,toml,os,time
from confdb.Tim_Api import *
from commen.Tcose import TestCase

class Request():
    """
    请求方式
    """

    def __init__(self):
        self.route=TestCase()
        rout=self.route.Route(os.path.abspath(os.curdir))
        file = rout + "\\conf\\url_conf.toml"
        self.toml = toml.load(file)
        self.time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.begin = requests.session()
        self.login="/api/mgr/signin"    #登录url
        self.signout="/api/mgr/signout" #退出登录
        self.login_user={} #登录所用的账号

    def Flogin(self,dict_rester={}):
        """
        执行登录，保持登录状态
        :return:
        """
        self.login_user=dict_rester
        return self.Post(Tim_api_login_byhy, self.login_user)

    def ExitLogin(self):
        """
        退出登录，用于释放的
        :return:
        """
        dict=self.login_user
        return self.Post(Tim_api_exit_login, dict)

    def Parm(self,request_type,dict_request={}):
        """
        返回请求所需参数
        """
        parm=""
        json={}
        data={}
        if request_type=="params":
            for key,value in dict_request.items():
                parm=parm+key+"="+value+"&"
        elif request_type=="data":
            data=dict_request
        elif request_type=="json":
            json=dict_request
        elif request_type=="":
            json={}
        else:
            raise("[Error]:Content-Type")
        return parm,json,data

    def ApiCheck(self,api):
        """
        校验接口参数
        :return:
        """
        try:
            Tim_api = eval(api)
        except SyntaxError:
            print(f"{self.time} [Error] api invalid syntax")
        return Tim_api

    def ApiLeft(self,api,dict_request={},dict_rester={}):
        """
        获取接口信息进行组建，并返回请求参数
        :return:
        """
        # 将接口模板数据转换为字典
        Tim_api = self.ApiCheck(api)
        #登录，保持登录态
        if Tim_api["url"] != self.login and Tim_api["url"] != self.signout:
            log=self.Flogin(dict_rester)
            #判断登录态是否成功
            if log["ret"]==0:
                print(f"{self.time} [info] Login succeeded")
            elif log["ret"]==1:
                print(f"{self.time} [info] Login succeeded")
            else:
                raise print(f"{self.time} [info] Login failed")
            url = Tim_api["api_type"] + "://" + self.toml["url"] + ":" + self.toml["port"] + Tim_api["url"]
            print(f'{self.time} [info] requests url:{url}')
            parm = self.Parm(Tim_api["Content-Type"], dict_request)
            print(f'{self.time} [info] requests parameter:{parm}')
        elif Tim_api["url"] == self.signout or Tim_api["url"] == self.login:
            url = Tim_api["api_type"] + "://" + self.toml["url"] + ":" + self.toml["port"] + Tim_api["url"]
            print(f'{self.time} [info] requests url:{url}')
            parm = self.Parm(Tim_api["Content-Type"], dict_request)
            print(f'{self.time} [info] requests parameter:{parm}')

        return parm[0],parm[1],parm[2],url

    def Repons(self,respones):
        """
        处理返回参数，返回信息
        打印状态码
        :return:
        """
        print(f"{self.time} [info] status code:{respones}")
        respones = respones.json()
        print(f'{self.time} [info] Return information:{respones}')
        return respones


    def Get(self,api,dict_request={},dict_rester={}):
        """
        get请求方式
        :return:
        """
        parm = self.ApiLeft(api,dict_request,dict_rester)
        respones = self.begin.get(url=parm[3], params=parm[0])
        respones=self.Repons(respones)
        # 退出登录，释放
        if parm[3][-len(self.login):] != self.login and parm[3][-len(self.signout):] != self.signout:
            self.ExitLogin()
        return respones

    def Post(self,api,dict_request={},dict_rester={}):
        """
        Post请求封装
        :param api:
        :param dict_request:
        :return:
        """
        parm = self.ApiLeft(api,dict_request,dict_rester)
        respones = self.begin.post(url=parm[3], data=parm[2],json=parm[1])
        respones=self.Repons(respones)
        # 退出登录，释放
        if parm[3][-len(self.login):] != self.login and parm[3][-len(self.signout):] !=self.signout:
            self.ExitLogin()
        return respones

    def Put(self,api,dict_request={},dict_rester={}):
        """
        Put请求封装
        :param api:
        :param dict_request:
        :return:
        """
        parm = self.ApiLeft(api, dict_request,dict_rester)
        respones = self.begin.put(url=parm[3], data=parm[2])
        respones = self.Repons(respones)
        # 退出登录，释放
        if parm[3][-len(self.login):] != self.login and parm[3][-len(self.signout):] != self.signout:
            self.ExitLogin()
        return respones

    def Delete(self,api,dict_request={},dict_rester={}):
        """
        delete请求封装
        :param api:
        :param dict_request:
        :return:
        """
        parm = self.ApiLeft(api, dict_request,dict_rester)
        respones = self.begin.delete(url=parm[3], params=parm[0],json=parm[1])
        respones = self.Repons(respones)
        # 退出登录，释放
        if parm[3][-len(self.login):] != self.login and parm[3][-len(self.signout):] != self.signout:
            self.ExitLogin()
        return respones