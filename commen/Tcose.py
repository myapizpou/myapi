import unittest,os,time,json

class TestCase(unittest.TestCase):
    Time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    touch=""
    def setUp(self):
        self.step=1 #记步骤

    def CreateJson(self):
        """
        创建json日志文件
        :return:
        """
        self.f = open(self.touch, 'w')
        return self.f

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

    def PrintJson(self,Prin={}):
        """
        打印执行日志
        :return:
        """
        f = open(self.touch)
        numm = json.load(f)
        f.close()
        numm.update(Prin)
        numm1 = json.dumps(numm)
        with open(self.touch, "w") as fw:
            fw.write(numm1)
        fw.close()


    def name(self,name):
        """
        打印执行人，也就是用例编写人
        :param name:
        :return:
        """
        rout = self.Route(os.path.abspath(os.curdir))
        file_json =f"\\report{self.Time}.json"
        dict_l={"case_name":name}
        self.touch=rout + "\\Jsonproject"+ file_json
        self.f = open(self.touch, 'w')
        dict_json = json.dumps(dict_l)
        self.f.write(dict_json)
        self.f.close()


    def show(self,string):
        """
        打印执行步骤
        :param string:
        :return:
        """
        print(f"Perform steps {self.step}：{string}")
        self.step+=1

    def tearDown(self):
        print('==============结束============')

