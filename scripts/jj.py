import time

import requests
import yaml

import urllib
from io import BytesIO
from PIL import Image
import sys


def text_image(image_path, con=1):
    if con == 1:
        # 默认使用网络图片
        image_file = BytesIO(urllib.request.urlopen(image_path).read())
    else:
        # 本地图片
        image_file = image_path
    image_data = Image.open(image_file)
    img = image_data  # 获取图片对象
    width = image_data.width  # 获取图片宽度
    height = image_data.height  # 获取图片高度
    gray_img = img.convert('L')  # 图片转换为'L'模式  模式“L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度
    scale = width // 200  # 图片缩放长度
    char_lst = ' .:-=+*#%@'  # 要替换的字符
    char_len = len(char_lst)  # 替换字符的长度

    for y in range(0, height, scale):  # 根据缩放长度 遍历高度
        for x in range(0, width, scale):  # 根据缩放长度 遍历宽度
            choice = gray_img.getpixel((x, y)) * char_len // 255  # 获取每个点的灰度  根据不同的灰度填写相应的 替换字符
            if choice == char_len:
                choice = char_len - 1
            sys.stdout.write(char_lst[choice] * 2)  # 写入控制台
        sys.stdout.write('\n')
        sys.stdout.flush()


def image_url(num):
    url = "http://j4.dfcfw.com/charts/pic6/"+num+".png"
    return url

while True:
    yaml_path = "../data/data.yaml"
    jj_list = []
    with open(yaml_path, "r", encoding="utf-8") as f:
        info = yaml.load(f, Loader=yaml.FullLoader)
        for i in info:
            url = "http://fundgz.1234567.com.cn/js/" + i + ".js"
            result = requests.get(url).text.replace("jsonpgz(", "").replace(");", "")
            jj_list.append(eval(result))
    new1 = sorted(jj_list, key=lambda e: e["gszzl"], reverse=True)
    new2 = sorted(jj_list, key=lambda e: e["gszzl"])



    print("\n" + "=" * 50)
    for dict in new1:
        if float(dict["gszzl"]) >= 0:
            print(dict["name"] + ":\t" + str(dict["gszzl"]))

    for dict in new2:
        if float(dict["gszzl"]) < 0:
            print(dict["name"] + ":\t" + str(dict["gszzl"]))
    time.sleep(60)


# url = "https://pc-index-skin.cdn.bcebos.com/hiphoto/58371244491.jpg"
# text_image(url)