import requests

from requests.cookies import RequestsCookieJar
# 定义一个全局session
s = requests.Session()


class testlogin():
    def __init__(self):
        self.s = requests.Session()

    def test_login(self):
        url = "http://127.0.0.1:80/api/mgr/signin"
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-platform': 'Windows',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Cookie': 'csrftoken = ftE3dWoJqtQx963qTSGEtPPD62a3dntwBQWBacLeot1E1ntBWX7DE75O6EhU53kg'
        }
        Search_cookie = {
            'JSESSIONID': '3E2ED9359E53D31FBD13FE2ADE9D20D2'
        }
        data = {'username': 'byhy', 'password': '88888888'}
        r = self.s.post(url, data=data, headers=headers)
        result = r.json()
        cookies_values = requests.utils.dict_from_cookiejar(self.s.cookies)
        print(f'cookies_values : {cookies_values}')
        print(type(cookies_values))
        cookies_skey = cookies_values['sessionid']
        cookies_jar = RequestsCookieJar()
        cookies_jar.set("sessionid", cookies_skey)
        print(cookies_jar)
        print(result)
        print(f"r.cookies: {r.cookies}")
        print(self.s)
        return cookies_jar


class testxx():
    def __init__(self):
        # self.s = testlogin().test_login()
        self.cookie = testlogin().test_login()
        print(f'cookie: {self.cookie}')
        self.s = requests.Session()


    def test01(self):
        url = "http://127.0.0.1:80/api/mgr/customers"
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-platform': 'Windows',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Cookie': 'csrftoken = ftE3dWoJqtQx963qTSGEtPPD62a3dntwBQWBacLeot1E1ntBWX7DE75O6EhU53kg'
        }
        Search_cookie = {
            'JSESSIONID': '3E2ED9359E53D31FBD13FE2ADE9D20D2'
        }
        data = {'action': 'add_customer', 'data': {'name': 'ds', 'phonenumber': '17674573105', 'address': 'dasasdasd'}}
        r = self.s.post(url, json=data, cookies=self.cookie, headers=headers)
        result = r.json()
        cookies_values = requests.utils.dict_from_cookiejar(self.s.cookies)
        print(f'cookies_values : {cookies_values}')
        print(self.s)
        print(f"r.cookies: {r.cookies}")
        print(result)

l = testxx()
l.test01()
