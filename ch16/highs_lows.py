import csv
from matplotlib import pyplot as plt
# 获取天气信息
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    
    # 打印元素的索引和值
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 获取第2列所有信息 并转为int型 这里直接执行会报错
    # highs = []
    # for row in reader:
    #     high = int(row[1])
    #     highs.append(high)