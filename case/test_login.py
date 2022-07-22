from case import *


class Login(TestCase):
    """
    创建用户
    """
    def setUp(self):
        self.tcose = TextCase()
        self.tcose.name("zpou")
        self.coss = TextClient()

    def test_run(self):
        self.coss.test_weather()

    def tearDown(self):
        CCom().base_last_step()


if __name__ == '__main__':
    unittest.main()
