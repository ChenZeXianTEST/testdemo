import datetime
import random
from scripts.taizhouOA import *
import requests
import hashlib

'''
    重定向接口:requests会直接跳转,导致无法找到界面
    1.请求中添加allow_redirects=False,关闭自动重定向
    2.获取result中的headers,返回字典格式
    3.获取headers中的location值,将其值当做新url进行访问,header与data不变
    4.该项目中有个参数org.apache.struts.taglib.html.TOKEN,后台会有校验,从HTML中获取,每次请求都是新token


'''


class SendEmail():
    def post_request(self):
        xh = self.time_md5()
        url = 'http://192.168.0.212:8080/zhbg/pages/form.do'
        headers = {
            'Cookie': 'JSESSIONID=8F423FC219AC692FE0C4E77B6107B9B5; ydzf_token=mrjvcb4EKAfdDLYNgItphUBb2HdbmuSCTEpnwSprie6pdraH44hlZcbmP3huYhKsp3zkLDqCKcPn_eEdhV4r8PPv5mRP5Mrhd6pZjvbnCuN4reduR-jTDNpOY3WUjQINjJpZQTyHJR88DAL1AKY9UztcZFWZF9JVmMOD3ufZkxSF4-CKUAzBfwCINzKZ56AXMY5uevKP0CSU9ncNrIx7SCt7hSWjpZfCGHFcPm7OQMvlhwsUeHmL1FQT6C2HNFywN85C-zMFyjorHL92mggHj2jyaNZJ9bu4qxQBYic0IA9c2HylDD9FAOyid3hVhZSRSLj9-TI44A0EWXnL4dGPaYeh2ftVSloVd24N6C-fZCW30XCZmUkJCFC1rQXckEnMvZL1M298b_sNWo5fxVfO0Q=='}

        for i in range(10):
            num = random.randint(0, 99999)
            bt = '标题' + str(num)
            html_token = Taizou().get_html_token()
            data = {'org.apache.struts.taglib.html.TOKEN': html_token,
                    'pagePath': '/pages/zhbg/yjpt/nwfjx.jsp', 'method': 'save',
                    'XH': xh, 'SFDSFS': '0', 'DSFSSJ': '', 'SFYDSFS': '0',
                    'SFCGJ': '0', 'REDIRECTURI': '/pages/zhbg/yjpt/nwfjxList.jsp', 'whileArea': 'JSR',
                    'JSR': '[{"userId":"linxiangyang","userName":"林向阳","sex":"true"}]', 'CSR': '', 'MSR': '',
                    'YJBT': bt, 'YJZW': num, 'YJNR': num, 'YXJ': 'PT',
                    'FJR': 'system'}
            result = requests.post(url, headers=headers, data=data, allow_redirects=False)
            print(result.text)
            print(result.headers)
            newurl = result.headers['Location']
            print(newurl)
            r = requests.post(newurl, headers=headers, data=data)
            Taizou().set_html_token(r)


    def time_md5(self):
        t = datetime.datetime.now()
        if t.month < 10:
            newtime = str(t.year)+'0'+str(t.month)
        else:
            newtime = str(t.year) + str(t.month)

        if t.day < 10:
            newtime = newtime + '0' + str(t.day)
        else:
            newtime = newtime + str(t.day)
        if t.minute < 10:
            newtime = newtime + '0' + str(t.minute)
        else:
            newtime = newtime + str(t.minute)
        if t.second < 10:
            newtime = newtime + '0'+str(t.second)
        else:
            newtime = newtime + str(t.second)
        hl = hashlib.md5()
        hl.update(newtime.encode(encoding='utf-8'))
        hl.hexdigest()
        return str(newtime+hl.hexdigest())


if __name__ == '__main__':
    a = SendEmail()
    a.post_request()

