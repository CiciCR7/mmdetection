import os
import shutil

data_root = r'/data/DS920/drone/wrg_20230208/jyz_dcc/dachicun/'
sub_dirs = ['dachicun_peiyu_202105_all', 'dachicun_zy_all', 'hxd_fzc_hy', 'ori_label07_zy_xj_424']
dis_dir = r'one_for_all'

for sub_dir in sub_dirs:
    print(sub_dir)
    jpg_dir = os.path.join(data_root, sub_dir, 'VOC2007', 'JPEGImages')
    jpg_list = os.listdir(jpg_dir)
    for jpg in jpg_list:
        print(jpg)
        shutil.move(os.path.join(jpg_dir, jpg), os.path.join(data_root, dis_dir, 'jpg', jpg))

    xml_dir = os.path.join(data_root, sub_dir, 'VOC2007', 'Annotations')
    xml_list = os.listdir(xml_dir)
    for xml in xml_list:
        print(xml)
        shutil.move(os.path.join(xml_dir, xml), os.path.join(data_root, dis_dir, 'xml', xml))


