# mmdetection

------训练一个目标检测模型的过程----------------
资源：jpg文件夹和xml文件夹
数据问题：
1、数据清洗
I.利用mmdetection/tools_wqq/xml_jpg.py来查找xml与jpg的对应关系，查询有没有不对应的情况；
II.利用tools_wqq/check_boxes.py进行数据清洗，查找不正确的boxes的xml。比如长宽等；
2、观察每种类别，知道类别的特点，以及数量
I.利用mmdetection/tools_wqq/get_voc_class.py来记录每种类别的名字（按xml中类别出现的顺序进行记录）；
II.利用mmdetection/tools_wqq/different_class_get_name.py来抽取资源里的同类的jpg以及xml，再导入LabelImg中进行观察其特点；
III.利用mmdetection/tools_wqq/count_class.py进行计算源xml里的每种类别的数目；
3、制作coco形式数据集
I.利用mmdetection/tools_wqq/cvpr_create_trainval_test.py根据源资源xml文件夹来按自定义比例制作训练集train.txt，trainval.txt以及测试集val.txt或者test.txt；txt里记录jpg的名字；
II.利用mmdetection/tools_wqq/cvpr_convert_to_coco_json_byTXT_id_from_1.py根据I中的txt把训练集预测试集的xml生成json形式；（注意：里面的类别名字只填写你想要的xml中的类别，不一定是要和总类别数一样，然后类别排序要和xml里出现的类别顺序一样）
4、训练的配置
I.建立mmdetection/mmdet/datesets/shudian.py，该文件定义自己的训练数据的类别名称，建立了类似于CocoDataset类别的ShudianDataset；（注意：在配置文件中的类别选项要改成自己建立的类别，类似于mmdetection/configs/_base_/datasets/coco_detection.py中，首行dataset_type=’CocoDataset’改为’ShudianDataset’）
II.建立mmdetection/mmdet/evaluation/下建立自定义评估文件（还未尝试）；
III.在mmdetection/configs/下选择合适模型，并根据模型顶部的_base_中的路径来查找相关联系文件进行修改；训练文件中修改的内容：num_class、数据集路径等；
5、训练与测试
I.训练
CUDA_VISIBLE_DEVICES=0 
python tools/train.py configs/faster_rcnn/faster-rcnn_r101_fpn_1x_coco.py
II.中断后继续
训练中断，继续接着上次的地方进行训练
CUDA_VISIBLE_DEVICES=0 
python tools/train.py configs/faster_rcnn/faster-rcnn_r101_fpn_1x_coco.py --resume
III.测试模型

python	tools/test.py	--weights		checkpoints/epoch_1.pth configs/faster_rcnn/faster-rcnn_r50_fpn_1x_coco.py
III.展现效果
python demo/image_demo.py demo/shudian.jpg --weights checkpoints/epoch_1.pth configs/faster_rcnn/faster-rcnn_r50_fpn_1x_coco.py
