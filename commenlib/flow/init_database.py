import traceback
from commenlib.mysql_api.commen import CSQLtest


class INITDatebase(CSQLtest):

    def flow_initialize_database(self, db={}):
        """
        初始化连接数据库
        mysql = {
            "type": "mysql",
            "library_name": "pymysql",
            "user": "root",
            "password": "test1234",
            "port": "3306",
            "ip": "192.168.3.36",
            "database": "ouy",
            "charset": "utf8"
        }
        :return:
        """
        b_ret = True
        try:
            b_ret, db_result = self.check.chenk_db_sql(db)
            if not b_ret:
                raise Exception("Database data connection error")
            self.init_database(db_result)
        except Exception as e:
            b_ret = False
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            return b_ret

    def flow_select_table(self, sql_str='', table_name='', where_str=''):
        """
        查询表所有内容
        sql_str: 查看key值
        table_name： 表名
        where_str： 条件
        :return:
        """
        b_ret = True
        select_result = []
        try:
            sql = f'select {sql_str} from {table_name} {where_str};'
            b_ret, select_result = self.query(sql)
        except Exception as e:
            b_ret = False
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            return b_ret, select_result

    def flow_insert_sql(self, table_name='', data_tuple='', where_str=''):
        """
        插入语句
        :return:
        """
        b_ret = True
        sql = f'insert {table_name}(id,value) values{data_tuple} {where_str};'
        b_ret, insert_result = self.execute(sql)

