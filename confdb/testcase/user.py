from confdb.testcase.commen import Integrate
import traceback


class TextClient(Integrate):
    """
    对用例或一个动作，多个接口的组合封装.
    我下面展示的都只封装了一个，接口没太多的原因;
    对步骤进行封装
    进行断言
    """

    def test_weather(self):
        """
        创建客户
        :param username:
        :param password:
        :return:
        """
        b_ret = False
        try:
            b_ret, weather_result = self.flow_weather()
            self.base_assert("create user", b_ret)
        except Exception as e:
            b_ret = False
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            return weather_result

