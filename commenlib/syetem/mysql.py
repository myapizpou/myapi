import records
from Public_variable.clog import *


class Msql(object):

    def __init__(self):
        self.database_str = None
        self.db = None
        self.Clog = CLOGS()

    def lsql(self, db):
        self.Clog.enter()
        b_ret = True
        self.database_str = db
        self.Clog.info(f'Initialize the connection to the database')
        self.Clog.info(f'b_ret value: {b_ret}')
        try:
            self.Clog.info(f'Connecting to a Database: {self.database_str}')
            self.db = records.Database(self.database_str)
            self.Clog.info(f'database value: {self.db}')
        except Exception as e:
            b_ret = False
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            self.Clog.info(f'b_ret value: {b_ret}')
            return b_ret

    def query_sql(self, sql_str):
        self.Clog.enter()
        b_ret = True
        dt = []
        self.Clog.info(f'b_ret value: {b_ret}')
        self.Clog.info(f'sql value: {sql_str}')
        try:
            rows = self.db.query(sql_str)
            self.Clog.info(f'query value: {rows}')
            dt = rows.as_dict()
            self.Clog.info(f'query table value: {dt}')
        except Exception as e:
            b_ret = False
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            self.Clog.info(f'b_ret value: {b_ret}')
            return b_ret, dt

    def bulk_query(self, sql_str):
        self.Clog.enter()
        b_ret = True
        try:
            self.db.bulk_query(sql_str)
        except Exception as e:
            b_ret = False
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            self.Clog.info(f'b_ret value: {b_ret}')
            return b_ret


