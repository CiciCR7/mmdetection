
import xml.etree.ElementTree as ET
import os

import cv2
import mmcv
from PIL import Image
import numpy as np
import shutil

check_dir = r"/data/DS920/shudian/shudian/20220115/2021bisaishuju/tongdaohuanjing/ImageSets/"
xml_root = os.path.join(check_dir, 'xml')
new_xml_root = os.path.join(check_dir, 'new_xml')
image_root = os.path.join(check_dir, 'jpg')
new_image_root = os.path.join(check_dir, 'new_jpg')
error_txt = os.path.join(check_dir, 'error_txt.txt')
class_list = []

xml_name_list = sorted(os.listdir(xml_root))
id = 0


def print_all_classes():
    all_name_list = []
    for xml_name in xml_name_list:
        print(f"{xml_name}")
        xml_path = os.path.join(xml_root, xml_name)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        for obj in root.findall("object"):
            name = obj.find("name").text
            all_name_list.append(name)
        print(all_name_list)


def check_hw():
    tranposed_name_lists = []
    for xml_name in xml_name_list:
        xml_path = os.path.join(xml_root, xml_name)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        size = root.find("size")
        width = int(size.find("width").text)
        height = int(size.find("height").text)
        image_path = os.path.join(image_root, xml_name[:-4] + ".jpg")
        img = cv2.imread(image_path, flags=(cv2.IMREAD_COLOR + cv2.IMREAD_IGNORE_ORIENTATION))
        h, w, _ = img.shape
        if height != h or width != w:
            print(width, w, height, h)
            print(f"{xml_name}'s h, w is tranposed.")
            tranposed_name_lists.append(xml_name)
    print(tranposed_name_lists)


def check_bbox():
    if not os.path.exists(new_xml_root):
        os.makedirs(new_xml_root)

    if not os.path.exists(new_image_root):
        os.makedirs(new_image_root)


    f = open(error_txt, 'w')

    for xml_name in xml_name_list:
        global id
        if id % 50 == 0:
            print('id:', id)
        id += 1
        flag = 0
        xml_path = os.path.join(xml_root, xml_name)
        tree = ET.parse(xml_path)
        root = tree.getroot()

        image_path = os.path.join(image_root, xml_name[:-4] + ".jpg")
        img = cv2.imread(image_path, flags=(cv2.IMREAD_COLOR + cv2.IMREAD_IGNORE_ORIENTATION))
        try:
            h, w, _ = img.shape
        except Exception:
            f.write(xml_name + ': jpg error!')
            print(xml_name, ': jpg error!')
            shutil.move(os.path.join(image_root, xml_name[:-4] + ".png"), os.path.join(new_image_root, xml_name[:-4] + ".png"))
            shutil.move(os.path.join(xml_root, xml_name[:-4] + ".xml"), os.path.join(new_xml_root, xml_name[:-4] + ".xml"))
            continue
        
        size_xml = root.find('size')
        width_xml = int(size_xml.find('width').text)
        height_xml = int(size_xml.find('height').text)
        if height_xml != h or width_xml != w:
            flag = 1
            print(xml_name, ':h/w error', width_xml, height_xml, w, h)
            f.write(xml_name+':h/w error\n')
            f.flush()

        for obj in root.findall("object"):
            bnd_box = obj.find("bndbox")
            bbox = [
                int(float(bnd_box.find("xmin").text)),
                int(float(bnd_box.find("ymin").text)),
                int(float(bnd_box.find("xmax").text)),
                int(float(bnd_box.find("ymax").text)),
            ]

            #if obj.find('name').text not in class_list:
            #    f.write(xml_name+':obj:'+obj.find('name').text+' not in list\n')
            #    f.flush()
            #    flag = 1

            if bbox[0] >= bbox[2] or bbox[1] >= bbox[3]:
                print(xml_name, ":bbox[0] >= bbox[2] or bbox[1] >= bbox[3]:", bbox)
                f.write(xml_name+":bbox[0] >= bbox[2] or bbox[1] >= bbox[3]\n")
                f.flush()
                flag = 1
            if bbox[3] > h or bbox[2] > w:
                print(xml_name, ":bbox[3] > h or bbox[2] > w:", bbox, h, w)
                f.write(xml_name+":bbox[3] > h or bbox[2] > w\n")
                f.flush()
                flag = 1
        if flag == 1:
            print(xml_name)
            tree.write(os.path.join(new_xml_root, xml_name))
            os.remove(os.path.join(xml_root, xml_name))

check_bbox()
