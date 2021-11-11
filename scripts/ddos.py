import random
import time

import requests
from lxml import etree



headers = {'Host': 'ssthjj.zhuhai.gov.cn',
           'Connection': 'keep-alive',
           'Pragma': 'no-cache',
           'Cache-Control': 'no-cache',
           'Upgrade-Insecure-Requests': '1',
           'DNT': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Referer': 'http://ssthjj.zhuhai.gov.cn/xxgkml/gzwj/flfg/index.html',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': "zh-CN,zh;q=0.9",
           'Cookie': '_gscu_2010100555=36439645ro4cos56; _gscbrs_2010100555=1; laravel_session=eyJpdiI6ImVZdmxkTzFnRnZtbytcL1pIaVRTWlhBPT0iLCJ2YWx1ZSI6IndXTVhpOGo4ODIzUkVHRW5yT1JFcXRNQ3RHSzZXbjZPaTh5QnNENVM0SDdQdUtBaDF2eityd214SDB4dEI4dVwvIiwibWFjIjoiMDZmOTVmMmI1NmQzNTE4OTJjMzNhZWQ3ZDlhOWY3M2VhOGI3MWJmYTY2MDNjNjQ0MzQ2ZTEzZjVjZjcxZWUwOSJ9; UM_distinctid=17d03679b43b6b-02f5eeb8f06a29-f7f1939-1fa400-17d03679b447e8; _trs_uv=kvrpx804_262_ijsr; CNZZDATA1278264395=1754022194-1636437714-null%7C1636437714; _gscu_1932448469=36440709kqil1u17; _gscbrs_1932448469=1; gkmlfront_session=eyJpdiI6IkE1a1BkOUdLOVR0Vkt3VFJjUzUxZlE9PSIsInZhbHVlIjoiejE3ZzdyUk9qVUZNWmZ0a0ZkenY3UStMc0JyYzVWQ0N4VFhXNXlKOXdrMk4yOVVKUUhQS2EwY3F1ZndVanErUSIsIm1hYyI6Ijk0YzVkZjM5ZjA5MWRmN2Y2ZjM0YWUyNzhmYzBhYTkyMDA1MmJiMTkxZDc2MjlmODUxOTFjY2ZjZDlmYTk0NGQifQ%3D%3D; _gscs_2010100555=364396452u5how56|pv:2; front_uc_session=eyJpdiI6ImkyMUNLSEluMTQrb1BcL2o2akZSbmhRPT0iLCJ2YWx1ZSI6IjEyeEd0Zlh2R1hSN1hVcEZacG83dEtxZUxxSkdlb0lqRXl2cjBHcnVpRVQ1REZiUjkzR2ZQcVlxUVwvWWUwVUNzIiwibWFjIjoiMDNmNTEwMDc4MzFkOGU0ZTYyNzVhODIyNWE2NTIyY2E5NWUwMTdlOWE3ZjdlMmZjNDc1ZTNmZTg4NDZkYTFkNiJ9; _gscs_1932448469=36440709t2uurw17|pv:6'}
for page_num in range(1, 21):
    if page_num == 1:
        url = 'http://ssthjj.zhuhai.gov.cn/xxgkml/gzwj/flfg/index.html'
    else:
        url = 'http://ssthjj.zhuhai.gov.cn/xxgkml/gzwj/flfg/index_'+str(page_num)+'.html'
    result = requests.get(url, headers=headers)
    result.encoding = 'utf-8'

    root = etree.HTML(result.content)
    for link_num in range(1, 16):
        html = root.xpath('//*[@id="listpage_right"]/div[2]/table/tbody/tr[' + str(link_num) + ']/td[1]/a/@href')
        text = root.xpath('//*[@id="listpage_right"]/div[2]/table/tbody/tr[' + str(link_num) + ']/td[1]/a/text()')
        print('文章标题:', str(text[0]).strip())
        print('hmtl', html)
        value = requests.get(url=html[0], headers=headers)
        print(value.text)
        time.sleep(1)
