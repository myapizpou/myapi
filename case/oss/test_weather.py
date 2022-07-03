from case import *


class Login(TestCase):
    """
    创建用户
    """

    def setUp(self):
        self.tcose = TextCase()
        self.tcose.name("zpou")  # 执行人
        self.coss = COS()

    def test_run(self):
        self.coss.flow_weather()


if __name__ == '__main__':
    unittest.main()
