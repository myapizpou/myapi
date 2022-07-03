from Public_variable.flowtest import *


class FlowUser(CNSflowtest):
    """
    用户登录-接口
    """

    def flow_login(self, update_dict=''):
        """
        登录接口
        :return:
        """
        self.Clog.enter()
        b_ret = False
        login_result = {}
        try:
            login_dict = {
                "username": "byhy",
                "password": "88888888"
            }
            if isinstance(update_dict, dict):
                login_dict.update(update_dict)
            else:
                print('TypeError: update_dict is not dict!')
            b_ret, login_result = self.api_login_byhy(login_dict)
            if not b_ret:
                raise Exception('Login failed')
        except Exception as e:
            b_ret = False
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            return b_ret, login_result

    def flow_mgr_signout(self):
        """
        登出接口
        :return:
        """
        self.Clog.enter()
        b_ret = False
        try:
            b_ret, signout_result = self.api_api_mgr_signout()
            if not b_ret:
                raise Exception('Logout failed')
        except Exception as e:
            b_ret = False
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            return b_ret, signout_result


