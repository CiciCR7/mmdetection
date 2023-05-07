#!/usr/bin/env python
# -*- coding:utf-8
# 版本校正V1.2,温招洋于7.25修改
# 该程序可获取所有标签名及数量

import xml.etree.ElementTree as ET
import os
import numpy as np
from tqdm import tqdm
#import matplotlib.pyplot as plt
import shutil

# xml文件路径
xmlpath =r'/data/DS920/shudian/shudian_2023/0421/JYZ-0421/wangqiqi/voc/train/Annotations'
classes = {}
#classes_picked = ['sqbx', 'jueyuanzi_06','dcc_sjb']
#classes_picked_dir = r'./classes_picked'
xmlnames=os.listdir(xmlpath)

for xmlname in tqdm(xmlnames):#遍历所有的文件
    if xmlname.endswith('.xml'):#如果是xml
      # print('当前xml文件名:',xmlname)
      tree = ET.parse(os.path.join(xmlpath,xmlname))#解析xml
      objs=tree.findall('object')
      for obj in objs:
        cls=obj.find('name').text
        #if cls in classes_picked:
        #   shutil.copy(os.path.join(xmlpath,xmlname), os.path.join(classes_picked_dir, xmlname))
        if cls not in classes.keys():
           classes[cls]=1
        else:
            classes[cls]+=1


    #print('当前统计 ',xmlname,'{:d}/{:d}'.format(xmlnames.index(xmlname)+1,len(xmlnames)))


index = []
values = []
for cls1 in classes.keys():
    print(cls1,'：',classes[cls1])
    index.append(cls1)
    values.append(classes[cls1])

#
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# plt.title('绝缘子', fontsize=10)
# plt.bar(index, values, width=0.7)
# plt.xticks(2 * index, rotation=45)  # 这里是调节横坐标的倾斜度，rotation是度数
# plt.xticks()
#
# # 显示柱坐标上边的数字
# for a, b in zip(index, values):
#    plt.text(a, b + 0.5, '%.0f' % b, ha='center', va='bottom', fontsize=5)  # fontsize表示柱坐标上显示字体的大小
#
# plt.savefig('./tongdao.jpg')
