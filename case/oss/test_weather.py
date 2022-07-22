from case import *


class Login(TestCase):
    """
    连接数据库
    """

    def setUp(self):
        self.tcose = TextCase()
        self.tcose.name("zpou")
        self.coss = SqlDemonstration()

    def test_run(self):
        # 初始化连接数据库
        self.coss.lianjie_database()
        # 查看数据
        self.coss.select_table()
        # 插入数据
        self.coss.table_insert()

    def tearDown(self):
        CCom().base_last_step()


if __name__ == '__main__':
    unittest.main()
