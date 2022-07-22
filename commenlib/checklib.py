from Public_variable.clog import *


class Check(object):
    """
    处理数据并校验的方法集合
    """
    def __init__(self):
        self.Clog = CLOGS()

    def chenk_db_sql(self, db):
        """
        校验连接数据库需要的必要参数是否存在，并返回连接数据库所需的格式
        :param db:
        :return:
        """
        self.Clog.enter()
        b_ret = True
        database_str = ''
        try:
            self.Clog.info(f"b_ret value: {b_ret}")
            # 判断数据库类型
            if db["type"] == gcf.DATABASE_TYPE_MYSQL:
                # 检查必要字段是否存在
                key = list(db.keys())
                for i in range(len(gcf.DATABASE_TYPE_MYSQL_LIST)):
                    if gcf.DATABASE_TYPE_MYSQL_LIST[i] not in key:
                        if gcf.DATABASE_TYPE_MYSQL_LIST[i] != "database":
                            b_ret = False
                            raise Exception(f'{gcf.DATABASE_TYPE_MYSQL_LIST[i]} nonentity')
                database_str = f'{gcf.DATABASE_MYSQL_LIBRARY}://{db["user"]}:{db["password"]}@{db["ip"]}:{db["port"]}'
                if db["database"] is not None:
                    database_str = database_str + f'/{db["database"]}'
                database_str = database_str + f'?charset={db["charset"]}'
        except Exception as e:
            b_ret = False
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            self.Clog.info(f"database value: {database_str}")
            return b_ret, database_str

