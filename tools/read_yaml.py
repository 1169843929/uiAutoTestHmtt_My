import yaml
import os
from config import BASE_PATH


def read_yaml(filename):
    arrs = []
    filepath = BASE_PATH + os.sep + 'data' + os.sep + filename
    with open(filepath,'r',encoding='utf-8') as f:
        # 解析 yaml 文件方法 yaml.safe_load(f)
        for data in yaml.safe_load(f).values():
            # print(tuple(data.values()))
            # 转为元祖
            arrs.append(tuple(data.values()))
        return arrs