import time
import requests
import yaml


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
