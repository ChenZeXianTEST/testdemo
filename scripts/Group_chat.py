import random
import time
import urllib
import requests
from io import BytesIO
from PIL import Image


class GroupChat:
    def __init__(self, username, pwd, teamid, taskid, count=0):
        self.username = username
        self.pwd = pwd
        self.teamid = teamid
        self.taskid = taskid
        self.cookie_str = self.login()
        self.count = count

    # 登录接口获取cookie
    def login(self):
        login_url = "http://120.236.164.111:9090/api/public/core/login"
        headers = {
            "Accept": "application/json, text/plain, */*"
        }
        body = {"username": self.username, "password": self.pwd, "remember": "false", "captcha": ""}
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

    # 批量新增用户
    def add_user(self, start, end):
        url = "http://120.236.164.111:9090/api/core/userManager/add"
        header = {'Cookie': self.cookie_str}
        phone_start = "13030150"
        for i in range(start, end):
            if len(str(i)) == 1:
                num = "00" + str(i)
            elif len(str(i)) == 2:
                num = "0" + str(i)
            else:
                num = str(i)
            phone_end = str(random.randint(100, 1000))
            body = {
                "content": "{\"UserID\":\"\",\"EnName\":\"test_" + num + "\",\"CnName\":\"测试" + num + "\",\"PWD\":\"69e8a3c05fe71ed81f69ef623c0eeabd\",\"EMail\":\"\",\"Status\":1,\"Phone\":\" " + phone_start+phone_end+" \",\"Sex\":\"\",\"lstGID\":[\"ydzf-13924350581698764801\"]}"}
            time.sleep(0.2)
            print(body)
            result = requests.post(url=url, headers=header, json=body)
            print(result.text)

    # 批量添加用户带群聊中
    def add_member(self, start, end):
        url = "http://120.236.164.111:9090/ydzf/api/ydzf/task/addMember"
        header = {'Cookie': self.cookie_str}
        for i in range(start, end):
            if len(str(i)) == 1:
                num = "00" + str(i)
            elif len(str(i)) == 2:
                num = "0" + str(i)
            else:
                num = str(i)
            body = {"taskid": self.taskid, "members": "[\"U000" + num + "\"]"}
            time.sleep(0.1)
            result = requests.post(url, headers=header, json=body)
            print(result.text)

    # 获取头条新闻
    def get_TT_news(self):
        url = "https://www.toutiao.com/api/pc/list/feed?channel_id=3189398996&min_behot_time=0&refresh_count=1&ca" \
              "tegory=pc_profile_channel&_signature=_02B4Z6wo00101dGCSZAAAIDABkRk6T3GnF3Rpk0AABSXNbLgfAW6H8m9-UXWfbs" \
              "Y0oxaT9Cjs2y6NoMWK57geUtPZF2SlDJNo-0QmIbsYkalO.F-7SXB2-oxjhNbTTY4CE6ERX3U6vHvikah8c"
        header = {
            "cookie": "tt_webid=6985415606028437005; tt_webid=6985415609195152903; "
                      "ttcid=afa58fe4fdf34d808c922c3dbe40081624; csrftoken=d832b484ef69dea0d736c9c8c1bb48fb; "
                      "passport_csrf_token_default=bc73d75f13cb3e0f1b127ca4ccfab430; passport_csrf_token=bc73d75f"
                      "13cb3e0f1b127ca4ccfab430; MONITOR_WEB_ID=6985415609195152903; __feed_out_channel_key=gallery; "
                      "s_v_web_id=verify_kr9zqy9c_qca3NmPW_zik9_4lkK_AArl_6P2Kf45yXhAf; ttwid=1%7CbRL7tWtZzJQuJLi_Y9tc"
                      "momPi7GXRMzqiNIKMVMSPSc%7C1626691899%7C68b8f7e0351422b8b3b66b6df441553dfad4b85cca95854effc018"
                      "d26ed50da4; tt_scid=X.qHKH1DkPMYNcCCyZwR9kiYkVFapRHU2fkHA2EWO-LTHft5ViKZ0vey0rPBrq7d7fdf"}
        result = requests.get(url=url, headers=header).json()
        return result

    # 获取头条图片
    def get_TT_image(self):
        url = "https://www.toutiao.com/api/pc/list/feed?channel_id=3189398996&min_behot_time=1626418823&refresh_" \
              "count=2&category=pc_profile_channel&_signature=_02B4Z6wo00101j0bd6wAAIDD6t1a1DCKOvo9P3MAAO.G35GWgM6" \
              "MI1dbETe-rN6orZHQS29nb-UECpOjP2z3VlTeMw4M7poqTQmTzmu7akObUFEv4UCyRYe4Gcw4uEAadZTB2uN2kxBbOx9Y65"
        header = {
            "cookie": "cookie: tt_webid=6985415606028437005; MONITOR_WEB_ID=e66ecef9-c828-46d6-9f6c-82b4c13e1f42;"
                      " tt_webid=6985415609195152903; ttcid=afa58fe4fdf34d808c922c3dbe40081624; s_v_web_id=verify_"
                      "kr5zrrxx_I7wwVTCK_l7VU_4YNt_91qL_Im8YKHgu2F7i; csrftoken=d832b484ef69dea0d736c9c8c1bb48fb; "
                      "ttwid=1%7CbRL7tWtZzJQuJLi_Y9tcmomPi7GXRMzqiNIKMVMSPSc%7C1626418817%7Cb66e4ba2fe21c47ff677768"
                      "18b90331b5caeaa544ae9dbbb67832a140bf88609; tt_scid=LTJ.6hdPMgY.DIGeyMPSSn52yqDnE0b-UqgzYn18Nu"
                      "6CNIG2dHicgYqZtDNm7AXOb481"}
        result = requests.get(url=url, headers=header).json()
        return result

    # 发生文本
    def sendMSG(self, value):
        new_value = str(value)
        url = "http://120.236.164.111:9090/ydzf/api/chitchat/sendMsg"
        header = {'Cookie': self.cookie_str}
        body = {"sendContent": "{\"body\":\"" + new_value + "\"}", "chitchatID": self.teamid,
                "msgType": "text",
                "opts": "{\"body\":\"" + new_value + "\"}"}
        result = requests.post(url=url, headers=header, json=body)
        print(result.text)

    # 发送头条新闻文本
    def sendMSG_news(self, public=0):
        url = "http://120.236.164.111:9090/ydzf/api/chitchat/sendMsg"
        header = {'Cookie': self.cookie_str}
        if public == 0:
            news_list = self.get_TT_news()
        else:
            news_list = public
        for news in news_list["data"]:
            if news.get('Abstract'):
                if len(news['Abstract']) != 0:
                    body = {"sendContent": "{\"body\":\"" + news["Abstract"] + "\"}","chitchatID": self.teamid,"msgType": "text","opts": "{\"body\":\"" + news["Abstract"] + "\"}"}
                    result = requests.post(url=url, headers=header, json=body)
                    print(result.text)
                    print("*" * 100)
                    num = random.random() * 10 % 5
                    time.sleep(num)

    # 发送新闻图片
    def sendMSG_image(self, width, height, return_url):
        url = "http://120.236.164.111:9090/ydzf/api/chitchat/sendMsg"
        header = {'Cookie': self.cookie_str}
        body = {
            "sendContent": "{\"body\":{\"type\":\"img\",\"size\":{\"width\":" + str(width) + " ,\"height\":" + str(
                height) + "},\"url\":\"" + return_url + "\"}}",
            "chitchatID": self.teamid, "msgType": "img",
            "opts": "{\"body\":{\"type\":\"img\",\"size\":{\"width\":" + str(width) + ",\"height\":" + str(
                height) + "},\"url\":\"" + return_url + "\"}}"}
        result = requests.post(url, json=body, headers=header).text
        print(result)
        print("*" * 100)

    # 上传图片到服务器
    def save_image(self, public=0):
        url = "http://120.236.164.111:9090/ydzf/api/ydzf/task/saveFile"
        header = {'Cookie': self.cookie_str}
        if public == 0:
            imagelist = self.get_image_list(self.get_TT_image())
        else:
            imagelist = public
        for image_url in imagelist:
            w, h, imagefile = self.load_image(image_url)
            filename = "image" + str(self.count) + ".jpg"
            files = {filename: imagefile}
            body = {"name": filename}
            result = requests.post(url=url, headers=header, json=body, files=files)
            save_image_return_filepath = result.json()
            return_url = save_image_return_filepath["url"]
            self.sendMSG_image(w, h, return_url)
            num = random.random() * 10 % 5
            # time.sleep(num)
            self.count += 1

    # 把图片写入内存返回宽高及二进制
    def load_image(self, url):
        image_file = BytesIO(urllib.request.urlopen(url).read())
        image_data = Image.open(image_file)
        output = BytesIO()
        if image_data.format == 'JPEG':
            image_data.save(output, format='JPEG')
        elif image_data.format == 'PNG':
            image_data.save(output, format='PNG')
        else:
            return 0
        w = image_data.width
        h = image_data.height
        image_data.close()
        data_bin = output.getvalue()
        output.close()
        return w, h, data_bin

    # 获取头条响应体中的图片
    def get_image_list(self, value):
        image_list_return = []
        for news in value["data"]:
            if news.get('image_list'):
                for image in news['image_list']:
                    image_list_return.append(image['url'])
        return image_list_return

    # 获取头条新闻中的文字与图片
    # def send_TT_text_and_image(self):
    #     image_list = []
    #     while True:
    #         R.acquire()
    #         time.sleep(1)
    #         result = self.get_TT_news()
    #         for news in result["data"]:
    #             if news.get('Abstract') and news.get('image_list'):
    #                 if len(news['Abstract']) != 0:
    #                     self.sendMSG(news['Abstract'])
    #                     for image in news['image_list']:
    #                         image_list.append(image['url'])
    #                     self.save_image(image_list)
    #                     self.sendMSG((threading.current_thread().name + str(self.count)))
    #                     image_list.clear()
    #                     self.sendMSG("*" * 50)
    #         R.release()


if __name__ == '__main__':
    teamid = 'demo-14228069275698503681'
    taskid = 'task-14228069275572674561'
    admin = GroupChat('admin', 'e9599f5c930953eeceac6cd2a31bc733', teamid, taskid)
    admin.add_user(100, 200)
    # yidui = GroupChat('yiduiB', 'dd12b5a27f0081df88eb4b4b3d08a03a', teamid, taskid)
    # erdui = GroupChat('erduiB', 'dd12b5a27f0081df88eb4b4b3d08a03a', teamid, taskid)
    # R = threading.Lock()
    # threads = []
    # try:
    #     threads.append(threading.Thread(target=admin.sendMSG_news, name='admin'))
    #     threads.append(threading.Thread(target=admin.save_image, name='admin'))
    #     threads.append(threading.Thread(target=yidui.save_image, name='yidui'))
    #     threads.append(threading.Thread(target=yidui.sendMSG_news, name='yidui'))
    #     threads.append(threading.Thread(target=erdui.save_image, name='erdui'))
    #     threads.append(threading.Thread(target=erdui.sendMSG_news, name='erdui'))
    #     for i in threads:
    #         i.start()
    # except:
    #     print("Error: 无法启动线程")
