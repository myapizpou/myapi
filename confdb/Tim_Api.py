"""Tim_api_get_apone=
{
    "url":"/mobile/get"   #地址
    "type"："get"   #请求类型,如：Get,Post
    "api_type":"http"  #协议类型,如http,https
    "request":[""]  #请求字段
    "reponses_type": "json"  #返回信息的类型,如json,html
    "Content-Type":"params" #参数类型,如：params,json,data
}
"""
#获取客户界面
Tim_api_get_apone="""
{
    "url":"/api/mgr/customers",
    "type":"GET",
    "api_type":"http",
    "request":{"action":"$action","pagenum":"$pagenum","pagesize":"$pagesize","keywords":"$keywords","_":"$_"},
    "reponses_type":"json",
    "Content-Type":"params",
}
"""

#登录接口
Tim_api_login_byhy="""
{
    "url":"/api/mgr/signin",
    "type":"Post",
    "api_type":"http",
    "request":{"username":"$username","password":"$password"},
    "reponses_type":"json",
    "Content-Type":"data",
}
"""

#创建用户
Tim_api_create_User="""
{
    "url":"/api/mgr/customers",
    "type":"Post",
    "api_type":"http",
    "request":{"action":"$action","data":$data},
    "reponses_type":"json",
    "Content-Type":"json",
}
"""
