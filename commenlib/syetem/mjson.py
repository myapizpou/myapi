from Public_variable.clog import *
import traceback
import json


class Mjson(object):
    def __init__(self):
        self.Clog = CLOGS()

    @staticmethod
    def format_int(str_input):
        format_result = None
        try:
            format_result = int(str_input)
        except Exception as e:
            format_result = str_input
        return format_result

    def get(self, str_json, get_path, list_get_key, b_check_exist=True):
        """
        :param str_json: dict格式，要获取的数据的dict
        :param get_path: 字符串格式，获取只的路径，如”/info/list“
        :param list_get_key: 列表格式，想要获取的key值，
        :param b_check_exist:
        :return:
        """
        self.Clog.info("Enter function : get()")
        self.Clog.info(f"Json : {str_json}")
        self.Clog.info(f"Get path : {get_path}")
        self.Clog.info(f"Get key : {list_get_key}")

        dict_result = {
            "result": True,
            "info": "Get successfully.",
            "data": None
        }
        dict_get_data = {}
        try:
            if len(list_get_key) == 0:
                dict_result["result"] = False
                dict_result["info"] = "Parameter list_get_key is null."
                self.Clog.info(f"Get result : {dict_result}")
                self.Clog.info(f"Leave function : get()")
                return dict_result
            list_get_path = get_path.split("/")
            self.Clog.info(f"Split the get path, value : {str(list_get_path)}")
            dict_json_temp = str_json
            self.Clog.info(f"Get Load : {str(dict_json_temp)}")
            for index, value in enumerate(list_get_path):
                if len(str(value)) != 0:
                    try:
                        format_int = self.format_int(str(value))
                        dict_json_temp = dict_json_temp[format_int]
                    except:
                        dict_json_temp = None
                        dict_result["result"] = False
                        dict_result["info"] = "Can not find the path from the jsondictionary."
                        self.Clog.info(f"Get result : {dict_result}")
                        self.Clog.info(f"Leave function : get()")
                        return dict_result
            self.Clog.info(f"Get the target  dictionary, value: {dict_json_temp}")
            for index, value in enumerate(list_get_key):
                try:
                    if dict_json_temp.__contains__(str(value)):
                        dict_get_data[str(value)] = dict_json_temp[str(value)]
                    else:
                        if b_check_exist:
                            dict_get_data = {}
                            dict_result["result"] = False
                            dict_result["info"] = f"Can not find the path from the dictionar. key {str(value)}"
                            dict_result["data"] = dict_get_data
                            self.Clog.info(f"Get result : {dict_result}")
                            self.Clog.info(f"Leave function : get()")
                            return dict_result
                        else:
                            dict_get_data[str(value)] = "key does not exist"
                except Exception as e:
                    dict_get_data = {}
                    dict_result["result"] = False
                    dict_result["info"] = f"Get the key value failed. key {str(value)}"
                    dict_result["data"] = dict_get_data
                    self.Clog.info(f"Get result : {dict_result}")
                    self.Clog.info(f"Leave function : get()")
                    return dict_result
            dict_result["result"] = True
            dict_result["info"] = f"Get successfully."
            dict_result["data"] = dict_get_data
            dict_result["data"] = dict_get_data
            self.Clog.info(f"Get result : {dict_result}")
            self.Clog.info(f"Leave function : get()")
            return dict_result
        except Exception as e:
            dict_get_data = {}
            dict_result["result"] = False
            dict_result["info"] = str(e.args[0])
            self.Clog.info(f"Get result : {dict_result}")
            self.Clog.info(f"Leave function : get()")
            return dict_result

    def for_json_get(self, json_data, yes_data, key, list_key):
        self.Clog.info("Enter function : for_json_get()")
        self.Clog.info(f"Json : {json_data}")
        self.Clog.info(f"Get yes_data : {yes_data}")
        self.Clog.info(f"Get key : {key}")
        self.Clog.info(f"Get list_key : {list_key}")
        flag = False
        json_result = {}
        try:
            self.Clog.info(f"list : {json_data['data'][list_key]}")
            for i in range(len(json_data['data'][str(list_key)])):
                if yes_data == json_data['data'][list_key][i][key]:
                    flag = True
                    break
                else:
                    flag = False
            json_result["exist"] = flag
            self.Clog.info(f"exist : {json_result['exist']}")
            json_result["data"] = {
                list_key: []
            }
            if flag:
                for j in range(len(json_data['data'][list_key])):
                    if yes_data == json_data['data'][list_key][j][key]:
                        self.Clog.info(f"data : {json_result['data']}")
                        json_result['data'][list_key].append(json_data['data'][list_key][j])
            else:
                self.Clog.info(f"No key was matched. Procedure")
            self.Clog.info(json_result)
        except Exception as e:
            json_result["exist"] = False
            self.Clog.info(f"{e.args[0]}")
            self.Clog.info(traceback.format_exc())
        finally:
            return json_result

    def get_list_json(self, dict_json, get_path, list_get_key=[], get_str_condition={}, b_check_exist=True):
        self.Clog.info("Enter function : get_list_json()")
        self.Clog.info(f"Json : {dict_json}")
        self.Clog.info(f"Get path : {get_path}")
        self.Clog.info(f"Get list_get_key : {list_get_key}")
        self.Clog.info(f"Get condition : {get_str_condition}")
        list_get_path = get_path.split("/")
        self.Clog.info(f"Split the get path, value : {str(list_get_path)}")
        list_path = ''
        for i in range(len(list_get_path)):
            if i !=0 and i !=len(list_get_path)-1:
                list_path += list_get_path[i] + '/'
            list_result = self.get(dict_json, list_path, [list_get_path.pop()])
            self.Clog.info(f"Get list : {list_result}")
            try:
                collect_result = {}
                key = list(get_str_condition.keys())
                list_get_path = get_path.split('/')
                list_key = list_get_path.pop()
                self.Clog.info(f"list_key : {list_key}")
                if len(key) == 0:
                    raise Exception('Please enter filter criteria')
                for j in range(len(key)):
                    if j == 0:
                        collect_result = self.for_json_get(list_result, get_str_condition[str(key[j])], str(key[j]), list_key)
                        if not collect_result["exist"]:
                            break
                    else:
                        collect_result = self.for_json_get(collect_result, get_str_condition[str(key[j])], str(key[j]), list_key)
                        if not collect_result["exist"]:
                            break
                self.Clog.info(f"collect_result : {collect_result}")
                if not collect_result["exist"]:
                    json_result = {
                        "exist": collect_result["exist"],
                        "data": collect_result["data"]
                    }
                else:
                    data_list_key = '/data/' + list_key + '/0'
                    list_get_key_result = self.get(collect_result, data_list_key, list_get_key)
                    json_result = {
                        "exist": collect_result["exist"],
                        "data": list_get_key_result["data"]
                    }
                self.Clog.info(f"json_result : {json_result}")
            except Exception as e:
                self.Clog.info(f"{e.args[0]}")
                self.Clog.info(traceback.format_exc())
            finally:
                return json_result

