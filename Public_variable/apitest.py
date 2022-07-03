from tc_play.requetes import Request
import requests
import traceback
from Public_variable.clog import *
from commen.cons import gcf
import commen


class COSapitest(object):
    """
    封装调用发送申请方法
    """
    def __init__(self):
        self.Requests = Request()
        self.begin = requests.session()
        self.Clog = CLOGS()

    def get(self, api, dict_request, param, header_update={}):
        try:
            if isinstance(header_update, dict):
                param[4].update(header_update)
            respones = self.begin.post(url=param[3], params=param[0], headers=param[4], cookies=param[6])
            if param[7]:
                self.Requests.team_requetes_cookie(self.begin)
            b_ret, respones_reslut = self.Requests.team_requetes_respones(api, dict_request, respones)
        except Exception as e:
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            return b_ret, respones_reslut

    def put(self, api, dict_request, param, header_update={}):
        try:
            if isinstance(header_update, dict):
                param[4].update(header_update)
            respones = self.begin.put(url=param[3], data=param[2], headers=param[4], cookies=param[6])
            if param[7]:
                self.Requests.team_requetes_cookie(self.begin)
            b_ret, respones_reslut = self.Requests.team_requetes_respones(api, dict_request, respones)
        except Exception as e:
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            return b_ret, respones_reslut

    def delete(self, api, dict_request, param, header_update={}):
        try:
            if isinstance(header_update, dict):
                param[4].update(header_update)
            respones = self.begin.delete(url=param[3], data=param[2], json=param[1], headers=param[4], cookies=param[6])
            if param[7]:
                self.Requests.team_requetes_cookie(self.begin)
            b_ret, respones_reslut = self.Requests.team_requetes_respones(api, dict_request, respones)
        except Exception as e:
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            return b_ret, respones_reslut

    def post(self, api, dict_request={}, header_update=''):
        try:
            param = self.Requests.team_requetes_apileft(api, dict_request)
            if param[5] == gcf.TMP_API_REQUEST_GET:
                respones_reslut = self.get(api, dict_request, param)
            elif param[5] == gcf.TMP_API_REQUEST_PUT:
                respones_reslut = self.put(api, dict_request, param)
            elif param[5] == gcf.TMP_API_REQUEST_DELETE:
                respones_reslut = self.delete(api, dict_request, param)
            else:
                if isinstance(header_update, dict) and header_update != {}:
                    param[4].update(header_update)
                respones = self.begin.post(url=param[3], data=param[2], json=param[1], headers=param[4], cookies=param[6])
                if param[7]:
                    self.Requests.team_requetes_cookie(self.begin)
                b_ret, respones_reslut = self.Requests.team_requetes_respones(api, dict_request, respones)
        except Exception as e:
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            return b_ret, respones_reslut

