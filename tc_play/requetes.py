import traceback
import requests
from commenlib.Tcose import TextCase
import string
from Public_variable.getpath import *
from commenlib.const import gcf
from Public_variable.clog import *
from commenlib import *
import commenlib
from requests.cookies import RequestsCookieJar


class Request(object):
    """
    请求方式
    """

    def __init__(self):
        self.route = TextCase()
        self.gpath = GetPath()
        self.Clog = CLOGS()
        self.begin = requests.session()
        self.cookie_z = None

    def team_requetes_param(self, request_type, dict_request={}):
        """
        返回请求所需参数
        """
        parm = ""
        json = {}
        data = {}
        try:
            if request_type == gcf.TMP_API_CONTENT_TYPE_PARAM:
                for key, value in dict_request[gcf.TMP_API_REQUEST].items():
                    parm = parm+key + "=" + value + "&"
            elif request_type == gcf.TMP_API_CONTENT_TYPE_DATA:
                data = dict_request[gcf.TMP_API_REQUEST]
            elif request_type == gcf.TMP_API_CONTENT_TYPE_JSON:
                json = dict_request[gcf.TMP_API_REQUEST]
            elif request_type == "":
                json = {}
            else:
                self.Clog.error(f"[Error]: {gcf.TMP_API_CONTENT_TYPE}")
        except Exception as e:
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            return parm, json, data

    def team_requetes_apileft(self, api, dict_request={}):
        """
        获取接口信息，并返回请求参数
        :return:
        """
        try:
            flag = False
            tmpl = string.Template(api)
            context = tmpl.safe_substitute(dict_request)
            contex = eval(context)
            self.Clog.info('interface message: ' + str(contex))
            # 获取配置文件中的数据
            ip = self.gpath.get_toml_param("url", "user_1")
            port = self.gpath.get_toml_param("port", "user_1")
            # 组成url
            if port == '':
                url = contex[gcf.TMP_API_TRPE] + gcf.API_SYMBOL + ip + contex[gcf.TMP_API_URL]
            else:
                url = contex[gcf.TMP_API_TRPE] + gcf.API_SYMBOL + ip + gcf.API_SYMBOL_M + port + contex[gcf.TMP_API_URL]
            self.Clog.info('requests url: ' + url)
            # 请求方式
            request_method = contex[gcf.TMP_API_REQUEST_TRPE].lower()
            if request_method in gcf.TMP_API_REQUEST_LIST:
                self.Clog.info(f'request method: {request_method}')
            else:
                raise Exception("The request mode is incorrect!")
            # 获取请求参数
            parm = self.team_requetes_param(contex[gcf.TMP_API_CONTENT_TYPE], contex)
            self.Clog.info('requests parameter: '+str(parm[2]))
            # 判断输入请求头
            if contex[gcf.TMP_API_LOCATION_INTERFACE] == gcf.TMP_API_LOGIN:
                headers = gcf.API_HEADER
                flag = True
                cookie = None
            else:
                headers = None
                flag = False
                cookie = self.cookie_z
            self.Clog.info('headers: ' + str(headers))
            self.Clog.info('cookie: ' + str(cookie))
        except Exception as e:
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            return parm[0], parm[1], parm[2], url, headers, request_method, cookie, flag

    def team_requetes_respones(self, tmp_api, dict_request,  respones):
        """
        处理返回参数，返回信息
        打印状态码
        :return:
        """
        b_ret = True
        self.Clog.info(f'b_ret value: {b_ret}')
        try:
            respones = respones.json()
            tmpl = string.Template(tmp_api)
            context = tmpl.safe_substitute(dict_request)
            contex = eval(context)
            key = list(contex[gcf.TMP_API_CYCLICAL_PATTERN][gcf.TMP_API_JUDGEMENT_CONDITION][gcf.TMP_API_RIGHT_OR_WRONG].keys())
            key_value = contex[gcf.TMP_API_CYCLICAL_PATTERN][gcf.TMP_API_JUDGEMENT_CONDITION][gcf.TMP_API_RIGHT_OR_WRONG][key[0]]
            if respones[key[0]] == key_value:
                b_ret = True
            else:
                b_ret = False
            self.Clog.info(f'In response to the results: {respones}')
            self.Clog.info(f'b_ret value: {b_ret}')
        except Exception as e:
            b_ret = False
            self.Clog.info(f'b_ret value: {b_ret}')
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            return b_ret, respones

    def team_requetes_cookie(self, cookie_param):
        """
        获取cookie
        :return:
        """
        try:
            cookies_values = requests.utils.dict_from_cookiejar(cookie_param.cookies)
            self.Clog.info(f'cookies_values : {cookies_values}')
            cookies_skey = cookies_values['sessionid']
            cookies_jar = RequestsCookieJar()
            cookies_jar.set("sessionid", cookies_skey)
        except Exception as e:
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            self.cookie_z = cookie_param.cookies



