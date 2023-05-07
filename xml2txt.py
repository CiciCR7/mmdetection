import os
import random

trainval_percent = 0.8
train_percent = 0.75
xmlfilepath = '/data/DS920/shudian/shudian_2023/0421/JYZ-0421/Annotations'
txtsavepath = '/data/DS920/shudian/shudian_2023/0421/JYZ-0421/wangqiqi'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('/data/DS920/shudian/shudian_2023/0421/JYZ-0421/wangqiqi/trainval.txt', 'w')
ftest = open('/data/DS920/shudian/shudian_2023/0421/JYZ-0421/wangqiqi/test.txt', 'w')
ftrain = open('/data/DS920/shudian/shudian_2023/0421/JYZ-0421/wangqiqi/train.txt', 'w')
fval = open('/data/DS920/shudian/shudian_2023/0421/JYZ-0421/wangqiqi/val.txt', 'w')

for i in list:
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