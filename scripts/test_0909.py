import copy

import pandas as pd


def read_excel():
    filepath = R"D:\南海移动执法PC端-测试用例.xlsx"
    data = pd.read_excel(filepath)
    base = []
    line_list = []
    base.append(list(data.columns.values)[0:6])
    odd_even = 0
    test_case = 4
    if test_case % 2 == odd_even:
        pass
    else:
        odd_even = 1
    for i in range(len(data)):
        num = 0
        id = 1
        if test_case % 2 == odd_even:
            pass
        else:
            odd_even = 1
        for i in data.loc[i].values:
            if num < test_case:
                line_list.append(i)
            else:
                if num == test_case:
                    if pd.isnull(i):
                        break
                    line_list.append(str(id) + '.' + i)
                if num == test_case + 1:
                    if pd.isnull(i):
                        break
                    line_list.append(str(id) + '.' + i)
                    id += 1
                if num >= test_case + 2:
                    if pd.isnull(i):
                        break
                    if num % 2 == odd_even:
                        line_list[test_case] = line_list[test_case] + '\n' + str(id) + '.' + i
                    else:
                        line_list[test_case + 1] = line_list[test_case + 1] + '\n' + str(id) + '.' + i
                        id += 1
            num += 1
        base.append(copy.deepcopy(line_list))
        line_list.clear()
    return base


df = pd.DataFrame(read_excel())
df.to_excel(R'D:\test.xlsx', sheet_name='new_sheet', index=False, header=False)
