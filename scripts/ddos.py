import os

ip_list = []


def joint_ip():
    for i in range(20, 256):
        for j in range(20, 256):
            ip_list.append('14.30.' + str(i) + '.' + str(j))


joint_ip()
for i in ip_list:
    with os.popen('ping ' + i, 'r') as f:
        text = f.read()
        if text.find('请求超时') < 1:
            print(i)
            print(text)
            print('*' * 100)
