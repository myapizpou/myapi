from commenlib.const import gcf
import os
import toml


class GetPath(object):
    """
    获取各种路径
    """

    def get_my_api_path(self):
        try:
            slipt_str = ""
            if gcf.MAC_SPLIT in os.getcwd():
                slipt_str = gcf.MAC_SPLIT
            elif gcf.WIN_SPLIT in os.getcwd():
                slipt_str = gcf.WIN_SPLIT
            pwd = os.getcwd().split(slipt_str)
            for i in range(len(pwd)):
                if pwd[i] in gcf.TEMP_FILE:
                    pth = ''
                    for j in range(len(pwd) - i):
                        pth = pth + gcf.OLD_PATH
        except Exception as e:
            raise Exception(f'{e.args[0]}')
        finally:
            return pth

    def get_log_path(self):
        """
        获取logs路径
        :return:
        """
        pth = self.get_my_api_path()
        return os.path.abspath(pth + gcf.GET_LOGS_PATH)

    def get_toml_path(self):
        """
        获取配置文件的conf地址
        :return:
        """
        pth = self.get_my_api_path()
        return os.path.abspath(pth + gcf.GET_CONF_PATH)

    def get_toml_param(self, get_key, toml_key):
        """
        获取配置文件的数据
        :return:
        """
        toml_path = self.get_toml_path() + gcf.TOML_NAME
        toml_param = toml.load(toml_path)
        return toml_param[toml_key][get_key]

    def get_const_path(self):
        """
        获取const位置
        :return:
        """
        pth = self.get_my_api_path()
        return os.path.abspath(pth + gcf.GET_CONST_PATH)




