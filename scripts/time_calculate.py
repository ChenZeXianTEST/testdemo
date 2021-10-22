import os
import time

import pandas as pd


def str_change_time(a):
    if a in '0000-00-00 00:00:00':
        return False
    timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(timeArray))


def count_day(day_list):
    sum = 0
    for i in day_list:
        sum += i
    time_stamp = sum / len(day_list)
    day = time_stamp / 86400
    print("目前修改了:" + str(len(day_list)) + "个bug，解决bug平均用时约:", round(day, 1), "天")  # round(number，2)保留小数点后两位


index = 0
path = R"C:\Users\admin\Desktop\bug"
for file in os.listdir(path):  # os.listdir()获取当前路径下的所有文件名
    file_path = os.path.join(path, file)  # os.path.join()拼接路径  data.info() 查看表的数据格式
    data = pd.read_csv(file_path)
    count = 0  # 记录没有解决的bug数
    day_list = []
    index += 1
    print(str(index) + ".", str(file).split("-")[0])
    for i in range(len(data['解决日期'])):
        if '陈则先' in str(data['解决者'].iloc[i]):
            continue
        start = data['创建日期'].iloc[i]
        end = data['解决日期'].iloc[i]
        start_time = str_change_time(start)
        end_time = str_change_time(end)
        if end_time is False:
            count += 1
            continue
        else:
            day_list.append(end_time - start_time)
    count_day(day_list)
    print("剩余" + str(count) + "个未修改")
    day_list.clear()
    print()
