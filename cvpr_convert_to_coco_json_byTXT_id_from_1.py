#!/usr/bin/python
# -*- coding:GBK -*-
# @Author: hbchen
# @Time: 2018-01-29 2020-10-9
# @Description: 

import os, sys, json

from xml.etree.ElementTree import ElementTree, Element


TXT_PATH = r'/data/DS920/shudian/shudian_2023/0421/JYZ-0421/wangqiqi/vocANDcoco/train.txt'
XML_PATH = r'/data/DS920/shudian/shudian_2023/0421/JYZ-0421/Annotations'
JSON_PATH = r'/data/DS920/shudian/shudian_2023/0421/JYZ-0421/wangqiqi/vocANDcoco/train.json'

json_obj = {}
images = []
annotations = []
categories = []
categories_list = []
image_id = 0
annotation_id = 0
catID = 0

# classes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11']
# classes = ['5', '22', '24', '282', '469', '127', '73', '771', '158', '365', '17',
#            '79', '53', '64', '70', '3', '716', '54', '46', '459',
#            '671', '84', '153', '291', '50', '8', '71', '25', '38',
#            '163', '53', '52', '82', '347', '448', '115', '66', '194',
#            '78', '26', '49', '7', '62', '36', '517', '278', '215',
#            '90', '96', '609', '386', '81', '85', '867', '151', '136',
#            '16', '123', '303', '105', '169', '152', '202', '415']
# classes = ['46', '158', '260', '365'] # yunfei_rice_202205
# classes = ['46', '73', '158', '260', '365', '567']  # yunfei_rice_202211
# classes = ['1', '2', '3', '4']  # yunfei_aphid_202211
# classes = ['46','158','260','365','670','671','672','567'] # yunfei_rice
# classes = ['282','127','73','260','158','365','17','79','53','54','50','52','78','26'] # yunfei_important_20220224
# classes = ['282','127','73','260','158','365','17','79','53','54','50','52','78','26','0'] # yunfei_important_stack
# classes = ['282', '260', '50', '78', '26']  # yunfei_important_less
# classes = ['0',] # yunfei_stack or all_zero
# classes = ['1', '2', '3', '4'] # yunfei_stack or all_zero
#classes = [
#    '79', '1035', '194', '127', '282', '20', '3', '26', '50', '78',
#    '66', '77', '70', '64', '98', '8', '53', '54', '716', '82',
#    '25', '169', '160', '1060', '330', '386', '44', '7', '52', '1061',
#    '1062', '49', '17', '1063', '365', '260', '46', '21', '158', '252',
#    '36', '81', '86', '5', '24', '22', '69', '67', '1064', '1065',
#    '1066', '39', '96', '71', '115']  # yunfei 55 classes

# classes = []  # yunfei_all_class
# for i in range(1, 1060):
#     classes.append(str(i))

#classes = [
#'jyz_jyh_yw', 'jyz_jyh_px', 'jyz_jyh_sh', 'jyz_jyh_tl', 'jyz_jyh_fz',
#    'jyz_jyh_qs', 'jyz_jyh_zc', 'jyz_fdjx_bx', 'jyz_fdjx_dj ', 'jyz_fdjx_zc',
#    'czjyz_ps', 'czjyz_zb', 'czjyz_zs', 'jyz_wh', 'sqps', 'gjgmxs',
#    'jyz_bljyz_zb'
#] ## drone_jyz

#classes = [
#'dachicun_fzc_zc', 'dachicun_fzc_xs', 'dachicun_fzc_px', 'dachicun_fzc_tl',
#    'dachicun_fzc_hy_01', 'dachicun_fzc_hy_02', 'dachicun_xj_zc',
#    'dachicun_xj_xs', 'dachicun_xj_qx', 'dachicun_xc_zc', 'dachicun_xc_xs',
#    'dachicun_fzc_hy_03', 'dachicun_fzc_sh'
#
#] ## drone_dcc

#classes = ['jyz_fdjx_bx', 'jyz_fdjx_dj', 'jyz_fdjx_zc', 'dachicun_fzc_hy_03'] # addition classes
#classes = ['010101021',  '010101061', '010101071', '010201041', '010202011',
# '010202021', '010301011', '010301021', '010301031', '010301041',
# '010401041', '010401051', '010401053', '010401061', '060101051'
#]

#classes = ['010101021', '010101061']  # yw_nc_1
#classes = ['010301011', '010301021'] # ps_wh_2
# classes = ['010401051', '060101051'] # xztl_tk_3
#classes = ['010101071', '010201041', '010202011', '010202021', '010301031', '010401041', '010401061'] # others_4

#classes = ['010401051', '010301051', '010401041'] # 20230321-xuexi/
#classes = ['fzcxs', '040500000', 'fzczc', '040501000', 'zcxs', 'xcxjzc','040501011','xcxjpy','fzctl','040500013','fzcpy','040100000']#20230326-fzy
#classes = ['lsqxz','xdazbdw','lmxs','lszc','lsqlm','lmazbgf','xdxs']
classes = ['jyz_bljyz_zc','xjj_xdzc','dcc_xcxj_zc','dcc_fzc_xs',
'dcc_fzc_zc','jyz_fhjyz_zc','fsss_fnss_fnczc','xjj_lmzc',
'dcc_uxls_zc','jyz_jyh_zc','dcc_uxgh_zc','dcc_lb_zc',
'dcc_nzxj_zc', 'jyz_czjyz_zc','dcc_zjgb_zc', 'dcc_zdxjgb_zc']
#classes = ['gttsyw', 'gttsxs', 'gtqls']

def read_xml(in_path):
    tree = ElementTree()
    tree.parse(in_path)
    return tree


def if_match(node, kv_map):
    for key in kv_map:
        if node.get(key) != kv_map.get(key):
            return False
    return True


def get_node_by_keyvalue(nodelist, kv_map):
    result_nodes = []
    for node in nodelist:
        if if_match(node, kv_map):
            result_nodes.append(node)
    return result_nodes


def find_nodes(tree, path):
    return tree.findall(path)


print("-----------------Start------------------")

xml_names = []
sum = 0

f = open(TXT_PATH)
lines = f.readlines()
for line in lines:
    line = line.strip("\r\n") + ".xml"
    #print line
    xml_names.append(line)
    sum = sum + 1
f.close()



for xml in xml_names:
    flag = False
    print("processing " + xml)
    tree = read_xml(XML_PATH + "/" + xml)
    object_nodes = get_node_by_keyvalue(find_nodes(tree, "object"), {})
    if len(object_nodes) == 0:
        image = {}
        file_name = os.path.splitext(xml)[0]
        image["file_name"] = file_name + ".jpg"
        width_nodes = get_node_by_keyvalue(find_nodes(tree, "size/width"), {})
        image["width"] = int(width_nodes[0].text)
        height_nodes = get_node_by_keyvalue(find_nodes(tree, "size/height"), {})
        image["height"] = int(height_nodes[0].text)
        image["id"] = image_id
        print(xml, "no object")
    else:
        image = {}
        file_name = os.path.splitext(xml)[0]
        image["file_name"] = file_name + ".jpg"
        width_nodes = get_node_by_keyvalue(find_nodes(tree, "size/width"), {})
        image["width"] = int(float(width_nodes[0].text))
        height_nodes = get_node_by_keyvalue(find_nodes(tree, "size/height"), {})
        image["height"] = int(float(height_nodes[0].text))
        image["id"] = image_id 

        name_nodes = get_node_by_keyvalue(find_nodes(tree, "object/name"), {})
        name_correct_flag = 0
        for name_node in name_nodes:
            if name_node.text in classes:
                name_correct_flag = 1
                break
        if name_correct_flag == 0:
            print(xml + 'not correct!')
            continue

        xmin_nodes = get_node_by_keyvalue(find_nodes(tree, "object/bndbox/xmin"), {})
        ymin_nodes = get_node_by_keyvalue(find_nodes(tree, "object/bndbox/ymin"), {})
        xmax_nodes = get_node_by_keyvalue(find_nodes(tree, "object/bndbox/xmax"), {})
        ymax_nodes = get_node_by_keyvalue(find_nodes(tree, "object/bndbox/ymax"), {})
       # print ymax_nodes
        for index, node in enumerate(object_nodes):
            annotation = {}
            segmentation = []
            bbox = []
            seg_coordinate = []

            if int(float(xmin_nodes[index].text)) == int(float(xmax_nodes[index].text)):
               continue
            if int(float(ymin_nodes[index].text)) == int(float(ymax_nodes[index].text)):
                continue

            seg_coordinate.append(int(float(xmin_nodes[index].text)))
            seg_coordinate.append(int(float(ymin_nodes[index].text)))
            seg_coordinate.append(int(float(xmin_nodes[index].text)))
            seg_coordinate.append(int(float(ymax_nodes[index].text)))
            seg_coordinate.append(int(float(xmax_nodes[index].text)))
            seg_coordinate.append(int(float(ymax_nodes[index].text)))
            seg_coordinate.append(int(float(xmax_nodes[index].text)))
            seg_coordinate.append(int(float(ymin_nodes[index].text)))
            segmentation.append(seg_coordinate)
            width = int(float(xmax_nodes[index].text)) - int(float(xmin_nodes[index].text))
            height = int(float(ymax_nodes[index].text)) - int(float(ymin_nodes[index].text))
            area = width * height

            bbox.append(int(float(xmin_nodes[index].text)))
            bbox.append(int(float(ymin_nodes[index].text)))
            bbox.append(width)
            bbox.append(height)

            annotation["segmentation"] = segmentation
            annotation["area"] = area
            annotation["iscrowd"] = 0
            annotation["image_id"] = image_id
            annotation["bbox"] = bbox
            if name_nodes[index].text not in classes:
                continue
            else:
                annotation["category_id"] = int(classes.index(name_nodes[index].text))
                flag = True
            annotation["id"] = annotation_id
            annotation_id += 1
            annotation["ignore"] = 0
            annotations.append(annotation)


    if flag:
        images.append(image)
        image_id += 1
        print("processing " + xml + ':' + str(image_id))

for i in classes:
    categorie = {}
    categorie["supercategory"] = None
    categorie["id"] = classes.index(i)
    categorie["name"] = i
    categories.append(categorie)


json_obj["images"] = images
json_obj["type"] = "instances"
json_obj["annotations"] = annotations
json_obj["categories"] = categories

f = open(JSON_PATH, "w")
json_str = json.dumps(json_obj)
f.write(json_str)

print("------------------End-------------------")
