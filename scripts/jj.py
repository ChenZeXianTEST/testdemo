import time
import requests
import yaml


def del_list_origin(list1):
    if len(list1) > 10:
        del list1[0]


jj_gz = {}
jj_list = []
yaml_path = "../data/data.yaml"
with open(yaml_path, "r", encoding="utf-8") as f:
    info = yaml.load(f, Loader=yaml.FullLoader)
while True:
    for i in info:
        url = "http://fundgz.1234567.com.cn/js/" + i + ".js"
        result = requests.get(url).text.replace("jsonpgz(", "").replace(");", "")
        try:
            jj_list.append(eval(result))
        except:
            print(result)
    for jj in jj_list:
        if jj["name"] in jj_gz.keys():
            jj_gz[jj["name"]].append(jj["gszzl"])
            del_list_origin(jj_gz[jj["name"]])
        else:
            jj_gz[jj["name"]] = []
            jj_gz[jj["name"]].append(jj["gszzl"])
    print("\n" + "=" * 50)
    for dict in sorted(jj_list, key=lambda e: e["gszzl"], reverse=True): # sorted() 对所有可迭代的对象进行排序操作, 默认升序 reverse = True 降序
        if float(dict["gszzl"]) >= 0:
            print(dict["name"] + ":" + str(jj_gz[dict["name"]]))
    for dict in sorted(jj_list, key=lambda e: e["gszzl"]):
        if float(dict["gszzl"]) < 0:
            print(dict["name"] + ":" + str(jj_gz[dict["name"]]))
    time.sleep(120)
    jj_list.clear()
