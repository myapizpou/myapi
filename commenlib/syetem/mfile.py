import os
import datetime
from time import strftime
import traceback
from Public_variable.getpath import *
from commenlib.const import gcf
from Public_variable.clog import *


class Mfile(object):

    def __init__(self):
        self.gpath = GetPath()
        self.Clog = CLOGS()

    def open_file(self, last=False):
        num = 1
        try:
            file_path = self.gpath.get_const_path() + gcf.STEP_FILE_NAME
            content = open(file_path, 'r')
            step_num = eval(content.read())
            num = step_num["step_num"]
            step_new = step_num
            if not last:
                step_new["step_num"] = step_num["step_num"] + 1
            else:
                step_new["step_num"] = 1
                step_new["b_ret"] = True
            content.close()
            content = open(file_path, 'w')
            content.write(str(step_new))
            content.close()
        except Exception as e:
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')
        finally:
            return num

    def start_end_time(self, end=False):
        try:
            file_path = self.gpath.get_const_path() + gcf.STEP_FILE_NAME
            content = open(file_path, 'r')
            step_num = eval(content.read())
            content.close()
            now = datetime.datetime.now()
            if not end:
                step_num["start"] = now.strftime("%Y-%m-%d %H:%M:%S")
            else:
                step_num["end"] = now.strftime("%Y-%m-%d %H:%M:%S")
            content = open(file_path, 'w')
            content.write(str(step_num))
            content.close()
        except Exception as e:
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')

    def count_step(self):
        try:
            self.Clog.info(f'#############################################')
            file_path = self.gpath.get_const_path() + gcf.STEP_FILE_NAME
            self.start_end_time(True)
            content = open(file_path, 'r')
            step_num = eval(content.read())
            content.close()
            self.Clog.info(f'步骤{self.open_file(True)}: 统计')
            if step_num["b_ret"]:
                self.Clog.info(f'The use case was successfully executed')
            else:
                self.Clog.info(f'Use case execution failed')
            param = ''
            for i in range(step_num["step_num"]):
                if i == step_num["step_num"]-2 and not step_num["b_ret"]:
                    param += f'{i+1}:失败  '
                else:
                    param += f'{i+1}:通过  '
            self.Clog.info(param)
            self.Clog.info(f'start: {step_num["start"]}')
            self.Clog.info(f'end: {step_num["end"]}')
            datebegin = datetime.datetime.strptime(step_num["start"], "%Y-%m-%d %H:%M:%S")
            dateend = datetime.datetime.strptime(step_num["end"], "%Y-%m-%d %H:%M:%S")
            diff = dateend - datebegin
            self.Clog.info(f'elapsed time: {diff}')
            self.Clog.info(f'case path: {self.gpath.get_log_path()}\{getFlist()}')
            self.Clog.info(f'log path: {self.gpath.get_log_path()}\{getFlist()}')
            self.Clog.info(f'#############################################')
        except Exception as e:
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')

    def error_step(self):
        try:
            file_path = self.gpath.get_const_path() + gcf.STEP_FILE_NAME
            content = open(file_path, 'r')
            step_num = eval(content.read())
            step_num["b_ret"] = False
            content.close()
            content = open(file_path, 'w')
            content.write(str(step_num))
            content.close()
        except Exception as e:
            self.Clog.error(f'{e.args[0]}')
            self.Clog.error(f'{traceback.format_exc()}')


