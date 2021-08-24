import urllib.request
from PIL import Image
from io import BytesIO
import os

import requests

# filepath = R"C:\Users\admin\Desktop\1.jpg"
# binfile = open(filepath, "rb")
# print(binfile)
# size = os.path.getsize(filepath)
# print(binfile.read())
# for i in range(size):
#     data = binfile.read(1) #每次输出一个字节
#     print(data)
# binfile.close()

def load_image(url):
    image_file = BytesIO(urllib.request.urlopen(url).read())
    image_data = Image.open(image_file)
    output = BytesIO()
    print(image_data.size)
    image_data.save(output, format='png')
    # print(image_data.format) #输出的不一定是JPEG也可能是PNG
    print(image_data.filename)
    image_data.close()
    data_bin = output.getvalue()
    output.close()
    return data_bin


def get_image_list(json):
    imagelist = []
    for imagelist in json:
        if imagelist.get("image_list"):
            for image in imagelist["image_list"]:
                for urllist in image['url_list']:
                    imagelist.append(urllist['url'])
    return imagelist

