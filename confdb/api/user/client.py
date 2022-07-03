from confdb.const.user.Tim_Api import *
from Public_variable.apitest import *


class ApiClient(COSapitest):
    """
    登录模块的api封装
    api可以根据产品的不同模块封装不同的py文件
    类名自定义，固定继承COSapitest
    """

    def api_get_apone(self, request_dict={}):
        """
        获取客户界面接口封装
        Tim_api_login_byhy:api模板名
        request_dict：传入的请求参数
        :return:
        """
        return self.post(Tim_api_mgr_customers, request_dict)
