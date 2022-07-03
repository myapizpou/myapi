from confdb.const.user.Tim_Api import *
from Public_variable.apitest import *


class ApiUser(COSapitest):
    """
    登录模块的api封装
    api可以根据产品的不同模块封装不同的py文件
    类名自定义，固定继承COSapitest
    """

    def api_login_byhy(self, request_dict={}):
        """
        登陆接口封装
        Tim_api_login_byhy:api模板名
        request_dict：传入的请求参数
        :return:
        """
        return self.post(Tim_api_mgr_signin, request_dict)

    def api_api_mgr_signout(self, request_dict={}):
        """
        登出接口封装
        :return:
        """
        return self.post(Tim_api_mgr_signout, request_dict)


