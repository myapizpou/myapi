from confdb.testcase.commen import Integrate
import traceback


class SqlDemonstration(Integrate):
    """
    连接数据库执行语句的演示
    """
    def lianjie_database(self):
        """
        初始化连接数据库
        :return:
        """
        b_ret = False
        try:
            mysql_db = {
                "type": "mysql",
                "library_name": "pymysql",
                "user": "root",
                "password": "test1234",
                "port": "3306",
                "ip": "192.168.3.36",
                "database": "ouy",
                "charset": "utf8"
            }
            self.base_step("lianjie_database")
            b_ret = self.sql.flow_initialize_database(mysql_db)
        except Exception as e:
            b_ret = False
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            self.base_assert("init database", b_ret)

    def select_table(self):
        """
        创建表
        :return:
        """
        b_ret = False
        try:
            self.base_step("select_table")
            b_ret, select_result = self.sql.flow_select_table('*', 'a_user')
        except Exception as e:
            b_ret = False
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            self.base_assert("insert", b_ret)

    def table_insert(self):
        """
        插入数据
        :return:
        """
        b_ret = False
        try:
            self.base_step("insert")
            b_ret, select_result = self.sql.flow_insert_sql()
        except Exception as e:
            b_ret = False
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            self.base_assert("insert", b_ret)
