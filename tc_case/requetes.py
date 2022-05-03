import requests,toml,os,time
from commen.Tcose import TextCase
import string

class Request():
    """
    请求方式
    """

    def __init__(self):
        self.route=TextCase()
        rout=self.route.Route(os.path.abspath(os.curdir))
        file = rout + "\\conf\\url_conf.toml"#配置文件地址
        self.toml = toml.load(file)
        self.time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.begin = requests.session()

    def Parm(self,request_type,dict_request={}):
        """
        返回请求所需参数
        """
        parm=""
        json={}
        data={}
        if request_type=="params":
            for key,value in dict_request['request'].items():
                parm=parm+key+"="+value+"&"
        elif request_type=="data":
            data=dict_request['request']
        elif request_type=="json":
            json=dict_request['request']
        elif request_type=="":
            json={}
        else:
            self.route.ErrorLog("[Error]:Content-Type")
        return parm,json,data

    def ApiCheck(self,api):
        """
        校验接口参数
        :return:
        """
        try:
            Tim_api = eval(api)
        except SyntaxError:
            self.route.ErrorLog("api invalid syntax")
        return Tim_api

    def ApiLeft(self,api,dict_request={}):
        """
        获取接口信息进行组建，并返回请求参数
        :return:
        """
        # 将接口模板数据转换为字典
        try:
            tmpl = string.Template(api)
            context = tmpl.safe_substitute(dict_request)
            contex = eval(context)
            url =contex["api_type"]+ "://" +self.toml["url"] + ":" + self.toml["port"] + contex["url"]
            self.route.Printlog('requests url: ' + url)
            parm = self.Parm(contex["Content-Type"], contex)
            self.route.Printlog('requests parameter: '+str(parm[2]))
        except SyntaxError:
            print("请检查api模板格式是否正确")
        except NameError:
            print("请检查api模板格式。如:传入字符串时是否是\'$str$\'")
        # url = Tim_api["api_type"] + "://" + self.toml["url"] + ":" + self.toml["port"] + Tim_api["url"]
        # self.route.Printlog('requests url: '+url)
        # parm = self.Parm(Tim_api["Content-Type"], dict_request)
        # self.route.Printlog('requests parameter: '+str(parm))
        return parm[0],parm[1],parm[2],url

    def Repons(self,respones):
        """
        处理返回参数，返回信息
        打印状态码
        :return:
        """
        respones = respones.json()
        self.route.Printlog("Return information: "+str(respones))
        return respones


    def Get(self,api,dict_request={}):
        """
        get请求方式
        :return:
        """
        parm = self.ApiLeft(api,dict_request)
        respones = self.begin.get(url=parm[3], params=parm[0])
        respones=self.Repons(respones)
        return respones

    def Post(self,api,dict_request={}):
        """
        Post请求封装
        :param api:
        :param dict_request:
        :return:
        """
        parm = self.ApiLeft(api,dict_request)
        respones = self.begin.post(url=parm[3], data=parm[2],json=parm[1])
        respones=self.Repons(respones)
        return respones

    def Put(self,api,dict_request={},dict_rester={}):
        """
        Put请求封装
        :param api:
        :param dict_request:
        :return:
        """
        parm = self.ApiLeft(api, dict_request)
        respones = self.begin.put(url=parm[3], data=parm[2])
        respones = self.Repons(respones)
        return respones

    def Delete(self,api,dict_request={}):
        """
        delete请求封装
        :param api:
        :param dict_request:
        :return:
        """
        parm = self.ApiLeft(api, dict_request)
        respones = self.begin.delete(url=parm[3], params=parm[0],json=parm[1])
        respones = self.Repons(respones)
        return respones