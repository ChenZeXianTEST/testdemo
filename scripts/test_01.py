import requests
import pytest


class Test01:

    def login(self):
        login_url = 'http://192.168.0.212:9090/api/public/core/login'
        headers = {
            "Accept": "application/json, text/plain, */*"}
        body = {"username": "admin", "password": "1", "remember": False, "captcha": ""}
        try:
            res = requests.post(url=login_url, headers=headers, data=body)
            cookies = res.cookies
            cookie = requests.utils.dict_from_cookiejar(cookies)
            return cookie
        except Exception as err:
            print('获取cookie失败：\n{0}'.format(err))

    def test_get(self):
        get_url = R'http://192.168.0.212:9090/api/gyy/yqyd/getData?methodName=getAllBaseDataNew&content={"key":"","currentPage":1,"pageSize":2,"ssqy":[],"hylx":[],"wrlx":[],"follow":-1,"sort":{"col":"jgdfCount","type":"desc"}}'
        cookie = self.login()
        headers = {"cookie": cookie}
        res = requests.get(url=get_url, headers=headers)
        res_result = res.json()
        if res.text.find("dz") < 0:
            assert 0
        else:
            print(2)
    # for i in res_result:
    #     if len(i["dwmc"]) >= 21:
    #         print(i["dwmc"] , len(i["dwmc"]))
    # lenght = 0
    # dzname = ""
    # gs = ""
    # for i in res_result:
    #     if len(i["dz"]) > lenght:
    #         lenght = len(i["dz"])
    #         dzname = i["dz"]
    #         gs = i["dwmc"]
    # print(dzname)
    # print(gs)

    if __name__ == '__main__':
        pytest.main("-s")
