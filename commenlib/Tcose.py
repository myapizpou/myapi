from Public_variable.clog import *
from commenlib import variable


class TextCase(object):

    def __init__(self):
        self.gpath = GetPath()
        self.Clog = None

    def caseuser(self, name):
        """
        统计出所有用例编写人和编写数量
        :param name:
        :return:
        """
        try:
            if len(variable.case_user) > 0:
                flag = True
                su = 0
                for i in range(len(variable.case_user)):
                    # 判断是否已有用例编写人，已有则增加用例数，无则初始化
                    if variable.case_user[i]["name"] == name:
                        # 发现相同，跳出循环
                        flag = False
                        su = i
                        break
                    elif variable.case_user[i]["name"] != name:
                        flag = True
                if flag:
                    # 初始化一个用例编写人信息
                    variable.case_user.append({"name": name, "count": 1})
                else:
                    # 增加一条用例统计
                    variable.case_user[su]["count"] = variable.case_user[su]["count"] + 1
                    variable.case_user[su].update({"count": variable.case_user[su]["count"]})
            elif len(variable.case_user) == 0:
                variable.case_user.append({"name": name, "count": 1})
            self.Clog.info(variable.case_user)
        except Exception as e:
            self.Clog.info(f'{e.args[0]}')

    def name(self, name):
        """
        打印执行人，也就是用例编写人
        :param name:
        :return:
        """
        try:
            # 统计所有用例编写人，并统计用例数
            # self.caseuser(name)
            self.Clog = CLOGS()
            dict_l = "Use case writer:" + name
            # 新建日志文件
            self.Clog.add()
            self.Clog.info(dict_l)
        except Exception as e:
            self.Clog.error(f'{e.args[0]}')


