from commenlib.syetem.mysql import Msql
from Public_variable.clog import *


class Usql(object):

    def __init__(self):
        self.msql = Msql()
        self.Clog = CLOGS()

    def init_database(self, db):
        """
        初始化连接数据库
        :return:
        """
        return self.msql.lsql(db)

    def query(self, sql_str):
        """
        执行语句
        :return:
        """
        return self.msql.query_sql(sql_str)

    def execute(self, sql_str):
        """
        执行语句
        :return:
        """
        return self.msql.bulk_query(sql_str)

