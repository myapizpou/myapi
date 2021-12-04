import unittest,os,time,sys

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
        a=0
        b=a-6
        for i in range(len(rou)):
            if rou[b:a]=="my_api":
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
            print(Prin)
            fw=open(globals()["touch"],"a")
            fw.write(Prin+"\n")
            fw.close()
        except FileNotFoundError:
            print("No such file or directory")


    def name(self,name):
        """
        打印执行人，也就是用例编写人
        :param name:
        :return:
        """
        if globals()["a"]==1:
            rout = self.Route(os.path.abspath(os.curdir))
            file_json =f"\\report{self.Time}.log"
            dict_l="Use case writer:"+name+"\n"
            globals()["touch"]=rout + "\\Jsonproject"+ file_json
            self.f = open(globals()["touch"], 'a')
            self.f.write(dict_l)
            self.f.close()
        globals()["a"]=globals()["a"]+1


    def show(self,string):
        """
        打印执行步骤
        :param string:
        :return:
        """
        self.Printlog("Perform steps "+str(globals()['step'])+": "+string)
        globals()["step"]+=1

    def tearDown(self):
        self.Printlog('==============last============')

