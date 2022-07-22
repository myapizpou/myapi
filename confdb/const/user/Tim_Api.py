"""Tim_api_get_apone=
{
    "url":"/mobile/get"   #地址
    "type"："get"   #请求类型,如：get,post
    "api_type":"http"  #协议类型,如http,https
    "request":[""]  #请求字段
    "reponses_type": "json"  #返回信息的类型,如json,html
    "Content-Type":"params" #参数类型,如：params,json,data
}
"""

# 登录接口
Tim_api_mgr_signin = """{
    commenlib.const.gcf.TMP_API_URL: "/api/mgr/signin",
    commenlib.const.gcf.TMP_API_REQUEST_TRPE: "post",
    commenlib.const.gcf.TMP_API_TRPE: commenlib.const.gcf.TMP_API_TRPE_HTTP,
    commenlib.const.gcf.TMP_API_LOCATION_INTERFACE: commenlib.const.gcf.TMP_API_LOGIN,
    commenlib.const.gcf.TMP_API_REQUEST:{
        "username":"$username",
        "password":"$password"
         },
    commenlib.const.gcf.TMP_API_REPONSES_TYPE_KEY: commenlib.const.gcf.TMP_API_REPONSES_TYPE_JSON,
    commenlib.const.gcf.TMP_API_CONTENT_TYPE: "data",
    commenlib.const.gcf.TMP_API_CYCLICAL_PATTERN: {
        commenlib.const.gcf.TMP_API_CYCLICAL_FALG: False,
        commenlib.const.gcf.TMP_API_JUDGEMENT_CONDITION:{
            commenlib.const.gcf.TMP_API_RIGHT_OR_WRONG:{
                "ret": 0
        }
    }
    },
}"""

# 登出接口
Tim_api_mgr_signout = """{
    commenlib.const.gcf.TMP_API_URL: "/api/mgr/signout",
    commenlib.const.gcf.TMP_API_REQUEST_TRPE: "post",
    commenlib.const.gcf.TMP_API_LOCATION_INTERFACE: commenlib.const.gcf.TMP_API_LOGOUT,
    commenlib.const.gcf.TMP_API_TRPE: commenlib.const.gcf.TMP_API_TRPE_HTTP,
    commenlib.const.gcf.TMP_API_REQUEST: {},
    commenlib.const.gcf.TMP_API_REPONSES_TYPE_KEY: commenlib.const.gcf.TMP_API_REPONSES_TYPE_JSON,
    commenlib.const.gcf.TMP_API_CONTENT_TYPE: "data",
    commenlib.const.gcf.TMP_API_CYCLICAL_PATTERN: {
        commenlib.const.gcf.TMP_API_CYCLICAL_FALG: False,
        commenlib.const.gcf.TMP_API_JUDGEMENT_CONDITION:{
            commenlib.const.gcf.TMP_API_RIGHT_OR_WRONG:{
                "ret": 0
        }
    }
    },
}"""

# 创建客户
Tim_api_mgr_customers = """{
    commenlib.const.gcf.TMP_API_URL: "/api/mgr/customers",
    commenlib.const.gcf.TMP_API_REQUEST_TRPE: "post",
    commenlib.const.gcf.TMP_API_LOCATION_INTERFACE: commenlib.const.gcf.TMP_API_PARAM,
    commenlib.const.gcf.TMP_API_TRPE: commenlib.const.gcf.TMP_API_TRPE_HTTP,
    commenlib.const.gcf.TMP_API_REQUEST: {
          "action": "$action",
          "data": {
            "name": "$name",
            "phonenumber": "$phonenumber",
            "address": "$address"
          }
        },
    commenlib.const.gcf.TMP_API_REPONSES_TYPE_KEY: commenlib.const.gcf.TMP_API_REPONSES_TYPE_JSON,
    commenlib.const.gcf.TMP_API_CONTENT_TYPE: "json",
    commenlib.const.gcf.TMP_API_CYCLICAL_PATTERN: {
        commenlib.const.gcf.TMP_API_CYCLICAL_FALG: False,
        commenlib.const.gcf.TMP_API_JUDGEMENT_CONDITION:{
            commenlib.const.gcf.TMP_API_RIGHT_OR_WRONG:{
                "ret": 0
        }
    }
    },
}"""
