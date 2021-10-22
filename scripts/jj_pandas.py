import time
import requests
import yaml

count = 0
yaml_path = "../data/data.yaml"
database = '../data/test.txt'
jj_list = []
name_list = []
with open(yaml_path, "r", encoding="utf-8") as f:
    info = yaml.load(f, Loader=yaml.FullLoader)
with open(database, 'a+', encoding='utf-8') as f:
    while True:
        for i in info:
            url = "http://fundgz.1234567.com.cn/js/" + i + ".js"
            rr = requests.get(url).text
            print(rr)
            print(type(rr))
            result = eval(rr.replace("jsonpgz(", "").replace(");", ""))
            print("转换成功！")
            jj_list.append(result['gszzl'])
            name_list.append(result['name'])
        if count == 0:
            f.writelines(str(name_list).replace('[', '').replace(']', '').replace(' ', '').replace("'", ''))
            f.write('\n')
        f.writelines(str(jj_list).replace('[', '').replace(']', '').replace(' ', '').replace("'", ''))
        f.write('\n')
        jj_list.clear()
        time.sleep(59)
        if count == 95:
            break
        count += 1
