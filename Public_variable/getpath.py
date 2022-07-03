from commen.cons import gcf
import os
import toml


class GetPath(object):
    """
    获取各种路径
    """

    def get_log_path(self):
        """
        获取logs路径
        :return:
        """
        return os.path.abspath(gcf.GET_LOGS_PATH)

    def get_toml_path(self):
        """
        获取配置文件的conf地址
        :return:
        """
        return os.path.abspath(gcf.GET_CONF_PATH)

    def get_toml_param(self, get_key, toml_key):
        """
        获取配置文件的数据
        :return:
        """
        toml_path = self.get_toml_path() + gcf.TOML_NAME
        toml_param = toml.load(toml_path)
        return toml_param[toml_key][get_key]




