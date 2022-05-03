import unittest,os,time,toml
from loguru import logger
from Public_variable.variable import *

class TextCase(unittest.TestCase):
    Time = time.strftime("%Y%m%d_%H%M%S", time.localtime())

    @classmethod
    def setUpClass(self):
        globals()["touch"]=None
        globals()["step"]=1
        globals()["a"] = 1

    def Route(self,rou):
        """
        返回路径
        :return:
        """
        rout=""
        rout_c=".."
        file=os.path.abspath(os.path.join(os.getcwd()))
        while True:
            if file[-4:]!="case":
                if file[-8:]=="tc_repot":
                    file = os.path.abspath(os.path.join(os.getcwd(), rout_c))
                    break
                file=os.path.abspath(os.path.join(os.getcwd(),rout_c))
                rout_c=rout_c+"/.."
            elif file[-4:]=="case":
                file = os.path.abspath(os.path.join(os.getcwd(), rout_c))
                break

        file=file+"\\conf\\url_conf.toml"#配置文件地址
        project = toml.load(file)
        a=0
        b=a-len(project["route"])
        for i in range(len(rou)):
            if rou[b:a]==project["route"]:
                rout=rou[:a]
                break
            a=a-1
            b = a - 6
        return rout

    def Printlog(self,Prin):
        """
        打印执行日志
        :return:
        """
        try:
            logger.info(Prin)
        except FileNotFoundError:
            print("No such file or directory")

    def ErrorLog(self,Prin):
        """
        打印错误执行日志
        :return:
        """
        try:
            logger.error(Prin)
        except FileNotFoundError:
            print("No such file or directory")

    def case_user(self,name):
        """
        统计出所有用例编写人和编写数量
        :param name:
        :return:
        """
        if len(case_user)>0:
            flag = True
            su=0
            for i in range(len(case_user)):
                #判断是否已有用例编写人，已有则增加用例数，无则初始化
                if case_user[i]["name"]==name:
                    #发现相同，跳出循环
                    flag=False
                    su=i
                    break
                elif case_user[i]["name"]!=name:
                    flag = True
            if flag==True:
                #初始化一个用例编写人信息
                case_user.append({"name": name, "count": 1})
            elif flag==False:
                #增加一条用例统计
                case_user[su]["count"]=case_user[su]["count"]+1
                case_user[su].update({"count":case_user[su]["count"]})
        elif len(case_user)==0:
            case_user.append({"name":name,"count":1})

    def name(self,name):
        """
        打印执行人，也就是用例编写人
        :param name:
        :return:
        """
        #统计所有用例编写人，并统计用例数
        self.case_user(name)
        if globals()["a"]==1:
            rout = self.Route(os.path.abspath(os.curdir))
            file_json =f"\\report{self.Time}.log"
            globals()["touch"] = rout + "\\Jsonproject" + file_json
            logger.add(globals()["touch"])
            dict_l="Use case writer:"+name
            logger.info(dict_l)
        globals()["a"]=globals()["a"]+1


    def show(self,string):
        """
        打印执行步骤
        :param string:
        :return:
        """
        logger.info("Perform steps "+str(globals()['step'])+": "+string)
        globals()["step"]+=1

    def tearDown(self):
        logger.info('==============last============')

