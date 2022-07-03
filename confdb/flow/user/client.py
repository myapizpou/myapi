from confdb.flow.user.user import FlowUser
import traceback


class FlowClient(FlowUser):
    """
    创建用户-接口
    """
    def flow_weather(self, update_dict=''):
        """
        获取客户信息
        :return:
        """
        self.Clog.enter()
        b_ret = False
        weather_result = {}
        try:
            # 登录
            self.flow_login()
            weather_dict = {
                "action": "add_customer",
                "address": "dasasdasd",
                "name": "ds",
                "phonenumber": "17674573105"
            }
            if isinstance(update_dict, dict):
                weather_dict.update(update_dict)
            else:
                self.Clog.info('TypeError: update_dict is not dict!')
            b_ret, weather_result = self.api_get_apone(weather_dict)
            if not b_ret:
                raise Exception('Failed to create a user!')
            # 释放
            self.api_api_mgr_signout()
        except Exception as e:
            b_ret = False
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            return b_ret, weather_result

