import random
from time import sleep

import requests

def get_result(url):
    result = requests.get(url).text
    return result

def spile_text(text):
    index = 0
    t = text.split('<div id="content">')[1]
    zheng = t.split('</div>')[0].replace('<br>', '').replace('<br/>', '').replace('&nbsp;', '')
    next_url = t.split('</div>')[1].split('"')
    biao = text.split('<h1>')[1].split('</h1>')[0]
    for i in range(len(next_url)):
        if next_url[i].find('下一章') > -1:
            index = i-1
            break
    if index == 0:
        return 0, biao, zheng
    return next_url[index], biao, zheng

def next_url(string):
    return 'http://www.biquxs520.com' + string


text = get_result('http://www.biquxs520.com/39711/63958141.html')
# spile_text(text)
with open(R'D:\testcode\data\test.txt', 'a+', encoding='utf-8')as f:
    while True:
        try:
            url, biao, zheng = spile_text(text)
        except:
            print("完结")
            exit()
        f.write(biao)
        f.write(zheng)
        f.write('\n')
        f.write('\n')
        if url == 0:
            print("*" * 100)
            print('完结')
            break
        text = get_result(next_url(url))
        print(biao)
        sleep(random.randint(1, 3))
