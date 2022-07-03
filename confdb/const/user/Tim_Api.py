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
    commen.cons.gcf.TMP_API_URL: "/api/mgr/signin",
    commen.cons.gcf.TMP_API_REQUEST_TRPE: "post",
    commen.cons.gcf.TMP_API_TRPE: commen.cons.gcf.TMP_API_TRPE_HTTP,
    commen.cons.gcf.TMP_API_LOCATION_INTERFACE: commen.cons.gcf.TMP_API_LOGIN,
    commen.cons.gcf.TMP_API_REQUEST:{
        "username":"$username",
        "password":"$password"
         },
    commen.cons.gcf.TMP_API_REPONSES_TYPE_KEY: commen.cons.gcf.TMP_API_REPONSES_TYPE_JSON,
    commen.cons.gcf.TMP_API_CONTENT_TYPE: "data",
    commen.cons.gcf.TMP_API_CYCLICAL_PATTERN: {
        commen.cons.gcf.TMP_API_CYCLICAL_FALG: False,
        commen.cons.gcf.TMP_API_JUDGEMENT_CONDITION:{
            commen.cons.gcf.TMP_API_RIGHT_OR_WRONG:{
                "ret": 0
        }
    }
    },
}"""

# 登出接口
Tim_api_mgr_signout = """{
    commen.cons.gcf.TMP_API_URL: "/api/mgr/signout",
    commen.cons.gcf.TMP_API_REQUEST_TRPE: "post",
    commen.cons.gcf.TMP_API_LOCATION_INTERFACE: commen.cons.gcf.TMP_API_LOGOUT,
    commen.cons.gcf.TMP_API_TRPE: commen.cons.gcf.TMP_API_TRPE_HTTP,
    commen.cons.gcf.TMP_API_REQUEST: {},
    commen.cons.gcf.TMP_API_REPONSES_TYPE_KEY: commen.cons.gcf.TMP_API_REPONSES_TYPE_JSON,
    commen.cons.gcf.TMP_API_CONTENT_TYPE: "data",
    commen.cons.gcf.TMP_API_CYCLICAL_PATTERN: {
        commen.cons.gcf.TMP_API_CYCLICAL_FALG: False,
        commen.cons.gcf.TMP_API_JUDGEMENT_CONDITION:{
            commen.cons.gcf.TMP_API_RIGHT_OR_WRONG:{
                "ret": 0
        }
    }
    },
}"""

# 创建客户
Tim_api_mgr_customers = """{
    commen.cons.gcf.TMP_API_URL: "/api/mgr/customers",
    commen.cons.gcf.TMP_API_REQUEST_TRPE: "post",
    commen.cons.gcf.TMP_API_LOCATION_INTERFACE: commen.cons.gcf.TMP_API_PARAM,
    commen.cons.gcf.TMP_API_TRPE: commen.cons.gcf.TMP_API_TRPE_HTTP,
    commen.cons.gcf.TMP_API_REQUEST: {
          "action": "$action",
          "data": {
            "name": "$name",
            "phonenumber": "$phonenumber",
            "address": "$address"
          }
        },
    commen.cons.gcf.TMP_API_REPONSES_TYPE_KEY: commen.cons.gcf.TMP_API_REPONSES_TYPE_JSON,
    commen.cons.gcf.TMP_API_CONTENT_TYPE: "json",
    commen.cons.gcf.TMP_API_CYCLICAL_PATTERN: {
        commen.cons.gcf.TMP_API_CYCLICAL_FALG: False,
        commen.cons.gcf.TMP_API_JUDGEMENT_CONDITION:{
            commen.cons.gcf.TMP_API_RIGHT_OR_WRONG:{
                "ret": 0
        }
    }
    },
}"""
