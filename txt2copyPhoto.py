import os
import shutil

data_dir = '/data/DS920/shudian/shudian_2023/0421/JYZ-0421'
train_dir = '/data/DS920/shudian/shudian_2023/0421/JYZ-0421/wangqiqi/vocANDcoco/train'
# val_dir = '/data/DS920/shudian/shudian_2023/0421/JYZ-0421/wangqiqi/voc/val'
test_dir = '/data/DS920/shudian/shudian_2023/0421/JYZ-0421/wangqiqi/vocANDcoco/test'
with open('/data/DS920/shudian/shudian_2023/0421/JYZ-0421/wangqiqi/vocANDcoco/train.txt', 'r') as f:
    for line in f:
        img_file = line.strip()
        # 拷贝图片文件
        src_path = os.path.join(data_dir, 'JPEGImages', img_file+'.jpg')
        dst_path = os.path.join(train_dir, 'JPEGImages', img_file+'.jpg')
        shutil.copyfile(src_path, dst_path)
        # # 拷贝对应的xml标注文件
        # src_path = os.path.join(data_dir, 'Annotations', img_file + '.xml')
        # dst_path = os.path.join(train_dir, 'Annotations', img_file + '.xml')
        # shutil.copyfile(src_path, dst_path)
    print('end')


with open('/data/DS920/shudian/shudian_2023/0421/JYZ-0421/wangqiqi/vocANDcoco/test.txt', 'r') as f:
    for line in f:
        img_file = line.strip()
        # 拷贝图片文件
        src_path = os.path.join(data_dir, 'JPEGImages', img_file+'.jpg')
        dst_path = os.path.join(test_dir, 'JPEGImages', img_file+'.jpg')
        shutil.copyfile(src_path, dst_path)
        # # 拷贝对应的xml标注文件
        # src_path = os.path.join(data_dir, 'Annotations', img_file + '.xml')
        # dst_path = os.path.join(test_dir, 'Annotations', img_file + '.xml')
        shutil.copyfile(src_path, dst_path)
    print('end3')
