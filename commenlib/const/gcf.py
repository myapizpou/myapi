import time

# 苹果路径分割符
MAC_SPLIT = '/'
# win路径分割符
WIN_SPLIT = '\\'
OLD_PATH = "../"
# 项目文件
TEMP_FILE = ['commenlib', 'case', 'case_report', 'conf', 'confdb', 'tc_play', 'tc_repot', 'logs', 'Public_variable']
# logs的绝对路径
GET_LOGS_PATH = "logs"
# conf地址
GET_CONF_PATH = "conf"
# const路径
GET_CONST_PATH = "commenlib/const"
# 步骤文件名
STEP_FILE_NAME = '/file_param.txt'
# 配置文件
TOML_NAME = "/url_conf.toml"
# 日志文件前缀
REPORT_NAME_QIAN = 'report'
# 日志文件名
REPORT_NAME = f'\\{REPORT_NAME_QIAN}{time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())}.log'
# 日志打印控制台颜色
LOG_COLOR = {"INFO": "black", "ERROR": "red"}
# 模板字段
TMP_API_URL = 'url'
# 接口请求类型，支持get、post、put、delete
TMP_API_REQUEST_TRPE = 'type'
TMP_API_REQUEST_POST = 'post'
TMP_API_REQUEST_PUT = 'put'
TMP_API_REQUEST_DELETE = 'delete'
TMP_API_REQUEST_GET = 'get'
TMP_API_REQUEST_LIST = [TMP_API_REQUEST_POST, TMP_API_REQUEST_PUT, TMP_API_REQUEST_DELETE, TMP_API_REQUEST_GET]
# http\https
TMP_API_TRPE = 'api_type'
TMP_API_TRPE_HTTP = 'http'
# 登录、登出和其他接口的标记
TMP_API_LOCATION_INTERFACE = 'location_interface'
# 登录使用
TMP_API_LOGIN = 'my_api_login'
# 登出使用
TMP_API_LOGOUT = 'my_api_logout'
# 平常接口使用
TMP_API_PARAM = 'my_api'
# 存放请求参数key
TMP_API_REQUEST = 'request'
# 接口返回参数的数据类型key
TMP_API_REPONSES_TYPE_KEY = 'reponses_type'
TMP_API_REPONSES_TYPE_JSON = 'json'
# 　接口发生请求的类型
TMP_API_CONTENT_TYPE = 'Content-Type'
TMP_API_CONTENT_TYPE_PARAM = 'param'
TMP_API_CONTENT_TYPE_DATA = 'data'
TMP_API_CONTENT_TYPE_JSON = 'json'
#  循环模式
TMP_API_CYCLICAL_PATTERN = 'cyclical_pattern'
# 判断返回flase还是ture的条件
TMP_API_JUDGEMENT_CONDITION = "judgement_condition"
TMP_API_CYCLICAL_FALG = "flag"
# 判断返回对错
TMP_API_RIGHT_OR_WRONG = "right_or_wrong"
# 请求头参数
API_HEADER = {
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-platform': 'Windows',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Cookie': 'csrftoken = ftE3dWoJqtQx963qTSGEtPPD62a3dntwBQWBacLeot1E1ntBWX7DE75O6EhU53kg'
}
API_SYMBOL = '://'
API_SYMBOL_M = ':'

# mysql
DATABASE_TYPE_MYSQL = 'mysql'
DATABASE_TYPE_MYSQL_LIST = ["type", "library_name", "charset", "user", "password", "port", "ip", "database"]
DATABASE_MYSQL_LIBRARY = 'mysql+pymysql'
# postgresql
DATABASE_TYPE_POSTGRESQL = 'postgresql'

