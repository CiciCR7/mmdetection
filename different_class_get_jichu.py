import xml.etree.ElementTree as ET
import os

import cv2
import mmcv
from PIL import Image
import numpy as np
import shutil

#源图片集和xml的位置
check_dir = r"/data/DS920/shudian/shudian/20220115/2021bisaishuju/jichu/ImageSets/"
xml_root = os.path.join(check_dir, 'xml')
image_root = os.path.join(check_dir, 'jpg')

#我的图片集和xml的位置
my_data_dir = r"/data/wangqiqi"

my_image_root = os.path.join(my_data_dir, 'jc')


image_class_jczwdj = os.path.join(my_image_root, 'jczwdj')
image_class_jclzym = os.path.join(my_image_root, 'jclzym')
image_class_jcps = os.path.join(my_image_root, 'jcps')
image_class_jccj = os.path.join(my_image_root, 'jccj')


if not os.path.exists(image_class_jczwdj):
    os.makedirs(image_class_jczwdj)

if not os.path.exists(image_class_jclzym):
    os.makedirs(image_class_jclzym)

if not os.path.exists(image_class_jcps):
    os.makedirs(image_class_jcps)
if not os.path.exists(image_class_jccj):
    os.makedirs(image_class_jccj)

xml_name_list = sorted(os.listdir(xml_root))#os.listdir()返回指定路径下的文件和文件夹列表。xml_name_list为所有xml文件列表


def different_class_get():
    all_name_list = []
    i1 = i2 = i3 = i4 = 0
    flag1 = flag2 = flag3 = flag4 = 1
    for xml_name in xml_name_list:
        #print(f"{xml_name}")
        xml_path = os.path.join(xml_root, xml_name)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        for obj in root.findall("object"):
            name = obj.find("name").text

            if name == 'jczwdj' and flag1 == 1:
                shutil.copy(os.path.join(image_root, xml_name[:-4] + ".jpg"),
                            os.path.join(image_class_jczwdj, xml_name[:-4] + ".jpg"))
                i1 = i1 + 1
                if i1 == 10:
                    flag1 = 0


            if name == 'jclzym' and flag2 == 1:
                shutil.copy(os.path.join(image_root, xml_name[:-4] + ".jpg"),
                            os.path.join(image_class_jclzym, xml_name[:-4] + ".jpg"))
                i2 = i2+1
                if i2 == 10:
                    flag2 = 0


            if name == 'jcps' and flag3 == 1:
                shutil.copy(os.path.join(image_root, xml_name[:-4] + ".jpg"),
                            os.path.join(image_class_jcps, xml_name[:-4] + ".jpg"))
                i3 = i3 + 1
                if i3 == 10:
                    flag3 = 0
            if name == 'jccj' and flag4 == 1:
                shutil.copy(os.path.join(image_root, xml_name[:-4] + ".jpg"),
                            os.path.join(image_class_jccj, xml_name[:-4] + ".jpg"))
                i4 = i4 + 1
                if i4 == 10:
                    flag4 = 0

            if i1 == i2 == i3 ==i4 == 10:
                break



            #all_name_list.append(name)

        #print(all_name_list)

different_class_get()