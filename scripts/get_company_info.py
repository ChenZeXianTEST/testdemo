import requests


def login(username, pwd):
    login_url = "http://120.236.164.111:9090/api/public/core/login"
    headers = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {"username": username, "password": pwd, "remember": "false", "captcha": ""}
    try:
        res = requests.post(url=login_url, headers=headers, data=body)
        cookies = requests.utils.dict_from_cookiejar(res.cookies)
        if len(cookies) == 0:
            print(res.text)
            raise Exception("cookies为空")
        cookie_str = ""
        length = 1
        for cookie in cookies:
            cookie_str = cookie_str + cookie + "=" + str(cookies[cookie])
            if length < len(cookies):
                cookie_str = cookie_str + ";"
            length += 1
        return cookie_str
    except Exception as err:
        print('获取cookie失败：{0}'.format(err))
        exit()


url = 'http://120.236.164.111:9090/api/ydzf/query/getEnterpriseList?condition={"page":{"pageNum":1,"pageSize":1}}'
header = {'Cookie': login("admin", "e9599f5c930953eeceac6cd2a31bc733")}
result = requests.get(url, headers=header).text
null = ""
result.replace("null", null)
dict1 = eval(result)

"""
cym 曾用名
dwmc 单位名称
dz  地址
FDDBR   法定代表人
XZQ 行政区
LXR 联系人
SJHM    手机号码
DHHM    电话号码
KYRQ    开业日期
QYZJ    统一社会信用代码
GYZCZ   工业总产值
ZZJGDM  组织机构代码
"""