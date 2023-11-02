import os
import pandas as pd
import csv

# 指定包含所有文本文件的文件夹路径
folder_path = '/Volumes/新加卷/飞秒实验数据/2023-11-2-数据处理/温度处理/处理'

# 初始化一个空的DataFrame以保存数据
combined_data = pd.DataFrame(columns=["Position"])
# 获取文件夹中的所有文本文件，并按数字大小排序
file_list = [filename for filename in os.listdir(folder_path) if filename.endswith(".txt")]
file_list = sorted(file_list, key=lambda x: int(x.split('.')[0]))


# 仅读取 "Position" 列的数据一次
with open(os.path.join(folder_path, file_list[0]), 'r') as file:
    lines = file.readlines()
    position_data = []
    for line in lines:
        if not line.startswith('#'):
            values = line.strip().split()
            if len(values) == 2:
                position_data.append(float(values[0]))
    combined_data["Position"] = position_data

    
# 循环遍历文件夹中的所有文件
for filename in file_list:
    file_path = os.path.join(folder_path, filename)
    # 从每个文本文件中读取数据并添加到DataFrame
    print("Processing at file : {}".format(filename))
    # 从每个文本文件中读取 Total Stress 数据并添加为一个列
    with open(file_path, 'r') as file:
        lines = file.readlines()
        total_stress_data = []
        for line in lines:
            if not line.startswith('#'):
                values = line.strip().split()
                if len(values) == 2:
                    total_stress_data.append(float(values[1]))
        combined_data[filename.split('.')[0]] = total_stress_data

# 将合并的数据保存为CSV文件
output_csv = '/Volumes/新加卷/飞秒实验数据/2023-11-2-数据处理/温度处理/combined_data.csv'
combined_data.to_csv(output_csv, index=False)

print("合并和保存数据完成。")
