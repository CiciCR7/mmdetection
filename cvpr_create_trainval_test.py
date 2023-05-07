#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author: hbchen
# @description: 数据预处理：根据xml划分trainval、train、val、test.txt

import os
import random

trainval_percent = 0.8
train_percent = 1

xmlfilepath = r'/data/DS920/shudian/shudian_2023/0421/JYZ-0421/Annotations'
txtsavepath = r'/data/DS920/shudian/shudian_2023/0421/JYZ-0421/wangqiqi/vocANDcoco'


# 历遍"Annotations"文件夹然后返回列表
total_xml = os.listdir(xmlfilepath)
total_xml.sort()
#total_xml.sort(key = lambda x: int(x[:-4]))

# 获取列表的总数
num = len(total_xml)
numlist = range(num)


tv = int(num * trainval_percent)
tr = int(tv * train_percent)

trainval = random.sample(numlist, tv)
trainval.sort()
test = list(set(numlist).difference(set(trainval)))
test.sort()

train = random.sample(trainval, tr)
train.sort()
val = list(set(trainval).difference(set(train)))
val.sort()

ftrainval = open(os.path.join(txtsavepath, 'trainval.txt'), 'w')
ftest = open(os.path.join(txtsavepath, 'test.txt'), 'w')
ftrain = open(os.path.join(txtsavepath, 'train.txt'), 'w')
fval = open(os.path.join(txtsavepath, 'val.txt'), 'w')

for i in numlist:
    # 使用切片方法获取文件名(去掉后缀".xml")
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
