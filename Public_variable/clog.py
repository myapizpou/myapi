import logging
import sys
import traceback
from Public_variable.getpath import *
import coloredlogs
from commenlib.const import gcf


def for_get_file(file_name, i):
    try:
        file_list_year = []
        for j in range(len(file_name)):
            time_list = file_name[j].split("-")
            if j == 0:
                file_list_year.append(file_name[j])
            else:
                file_list_year_int = int(file_list_year[0].split("-")[i][:2])
                if int(time_list[i][:2]) > file_list_year_int:
                    file_list_year = []
                    file_list_year.append(file_name[j])
                elif int(time_list[i][:2]) == file_list_year_int:
                    file_list_year.append(file_name[j])
    except Exception as e:
        raise Exception("Failed to obtain the latest logs. Procedure")
    finally:
        return file_list_year


def getFlist():
    try:
        # 获取所有日志文件
        gpath = GetPath()
        rout = gpath.get_log_path()
        files = os.listdir(rout)
        # 得到最新的日志文件
        file_name = []
        for i in range(len(files)):
            if files[i] != '__init__.py':
                file_name.append(files[i])
        file_list_year = []
        for j in range(len(file_name)):
            time_list = file_name[j].split("-")
            if j == 0:
                file_list_year.append(file_name[j])
            else:
                file_list_year_int = int(file_list_year[0].split("-")[0][len(gcf.REPORT_NAME_QIAN):])
                if int(time_list[0][len(gcf.REPORT_NAME_QIAN):]) > file_list_year_int:
                    file_list_year = []
                    file_list_year.append(file_name[j])
                elif int(time_list[0][len(gcf.REPORT_NAME_QIAN):]) == file_list_year_int:
                    file_list_year.append(file_name[j])
        file_list_month = for_get_file(file_list_year, 1)
        file_list_day = for_get_file(file_list_month, 2)
        file_list_shi = for_get_file(file_list_day, 3)
        file_list_fen = for_get_file(file_list_shi, 4)
        file_list_miao = for_get_file(file_list_fen, 5)
    except Exception as e:
        raise Exception("Failed to obtain the latest logs. Procedure")
    finally:
        return file_list_miao[0]


class Logger(object):
    def getlog(self, logname, loglevel):
        """
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        """
        try:
            # 创建一个logger
            self.logger = logging.getLogger()
            self.logger.setLevel(loglevel)
            # logging.basicConfig(stream=sys.stdout)
            # 创建一个handler，用于写入日志文件
            fh = logging.FileHandler(logname, encoding="UTF-8")
            fh.setLevel(loglevel)
            if not self.logger.hasHandlers():
                # 再创建一个handler，用于输出到控制台
                ch = logging.StreamHandler()
                ch.setLevel(loglevel)
                # 定义handler的输出格式
                # formatter = logging.Formatter('[%(levelname)s]%(asctime)s: %(message)s', log_colors=log_colors_config)
                formatter = logging.Formatter('[%(levelname)s]%(asctime)s: %(message)s')
                fh.setFormatter(formatter)
                ch.setFormatter(formatter)
                # 给logger添加handler
                self.logger.addHandler(fh)
                self.logger.addHandler(ch)
            logging.shutdown()
        except Exception as e:
            raise Exception("Logging initialization failed")
        finally:
            return self.logger


class CLOGS(object):
    """
    一些日志的方法
    """

    def __init__(self):
        self.gpath = GetPath()

    def add(self):
        """
        新建日志文件
        :return:
        """
        try:
            rout = self.gpath.get_log_path()
            file_path = rout + gcf.REPORT_NAME
            ulog = Logger().getlog(file_path, logging.DEBUG)
            ulog.info("#################################################################")
            ulog.info("Perform log")
            ulog.info("#################################################################")
        except Exception as e:
            raise Exception("Failed to create a log file. Procedure")

    def info(self, log_str):
        """
        打印平常日志
        :return:
        """
        try:
            file_path = getFlist()
            try:
                funcname = sys._getframe().f_back.f_code.co_name
                linenumber = sys._getframe().f_back.f_lineno
                ulog = Logger().getlog(self.gpath.get_log_path() + '//' + file_path, logging.DEBUG)
                ulog.info(f"{funcname}:{linenumber}:{log_str}")
            except Exception as e:
                ulog.error(f"{log_str}")
        except Exception as e:
            raise Exception("Description Failed to output common logs")

    def error(self, log_str):
        try:
            file_path = getFlist()
            try:
                funcname = sys._getframe().f_back.f_code.co_name
                linenumber = sys._getframe().f_back.f_lineno
                ulog = Logger().getlog(self.gpath.get_log_path() + '//' + file_path, logging.DEBUG)
                ulog.error(f"{funcname}:{linenumber}:{log_str}")
            except Exception as e:
                ulog.error(f"{log_str}")
        except Exception as e:
            raise Exception("Description Failed to output common logs")

    def enter(self, depth=1, log_swicth=True, skip=[]):
        try:
            file_path = getFlist()
            ulog = Logger().getlog(self.gpath.get_log_path() + '//' + file_path, logging.DEBUG)
            if log_swicth:
                ulog.info('Enter function : {func}()'.format(func=sys._getframe(depth).f_code.co_name))
                if str(skip).lower() == 'all':
                    pass
                else:
                    dict_params = dict(sys._getframe(1).f_locals)
                    for k in dict_params:
                        if str(k).lower() == "self" or str(skip).lower() == "log_switch" or k in skip:
                            continue
                        val = dict_params.get(k)
                        if len(str(val)) == 0:
                            val = 'value is empty.'
                        ulog.info('Input parameter : {k}, value : {val}'.format(k=k, val=val))
        except:
            ulog.info(traceback.format_exc())


