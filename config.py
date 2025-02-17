import pymysql
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

import paddle
from paddleseg.core.infer import predict
from mymodel import MySegNet, MyCFNet

import cv2
import copy
import numpy as np



# 连接数据库
def connect_database():
    conn = pymysql.connect(host='192.168.37.128', user='root', password='123', database='glu_diag_sys', port=3307)
    return conn


class Account:
    def __init__(self, account_id=0, password='', account_name=''):
        self.account_id = account_id
        self.password = password
        self.account_name = account_name

# 给当前用户设一个初始值
USER_NOW = Account()


Base = declarative_base()
class GlaucomaRecord(Base):
    __tablename__ = 'glaucoma_records'
    record_id = Column(Integer, primary_key=True, autoincrement=True)  # 记录编号
    record_result = Column(String(255), nullable=False)  # 诊断结果(non-GON或GON)
    record_time = Column(DateTime, default=datetime.utcnow, nullable=False)  # 诊断时间
    resource_img_address = Column(String(255), nullable=False)  # 诊断原图地址
    result1_img_address = Column(String(255), nullable=False)  # 诊断结果图1地址
    result2_img_address = Column(String(255), nullable=False)  # 诊断结果图2地址
    message = Column(String(255), nullable=False)  # 诊断信息


# 分割模型加载
def seg_model_load(model_path):
    # 初始化模型，这里以UNet为例
    model = MySegNet(num_classes=3)
    # 加载预训练模型参数
    model.set_dict(paddle.load(model_path))
    # 将模型设置为评估模式
    model.eval()
    return model

# 分类模型加载
def classfication_model_load(model_path):
    # 初始化模型，这里以UNet为例
    model = MyCFNet(num_classes=2)
    # 加载预训练模型参数
    model.set_dict(paddle.load(model_path))
    # 将模型设置为评估模式
    model.eval()
    return model

# 获取模型结果
def get_seg_result(model, img_path):
    # 通过模型直接进行推理和输出
    result = predict(model, img_path)
    seg_map = result['pred'].astype(np.uint8).squeeze()

    # 构造带分割区域的原图
    # 读取原图
    vis_result2 = cv2.imread(img_path)

    # 绘制类别 1 的绿色轮廓
    seg_map_class1 = (seg_map == 1).astype(np.uint8)  # 提取类别 1 的二值图
    contours_class1, _ = cv2.findContours(seg_map_class1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(vis_result2, contours_class1, -1, (0, 255, 0), thickness=2)  # 设置轮廓颜色为绿色

    # 绘制类别 2 的蓝色轮廓
    seg_map_class2 = (seg_map == 2).astype(np.uint8)  # 提取类别 2 的二值图
    contours_class2, _ = cv2.findContours(seg_map_class2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(vis_result2, contours_class2, -1, (255, 0, 0), thickness=2)  # 设置轮廓颜色为蓝色

    # 保存结果图
    cv2.imwrite('demo/tmp/images_tmp.jpg', vis_result2)

    # 通过像素点个数计算杯盘比
    result_copy = copy.deepcopy(result)
    numpy_data = result_copy.pred_sem_seg.numpy().data
    cup_count = np.sum(numpy_data == 1)
    disc_count = np.sum(numpy_data == 2)

    ratio = round(cup_count / (disc_count + cup_count), 5)

    return result, vis_result2, ratio

# 获取模型结果
def get_classfication_result(model, img_path):
    # 读取图像并进行预处理
    image = cv2.imread(img_path)
    image = image.astype(np.float32) / 255.0  # 归一化
    image = np.expand_dims(image, axis=0)  # 增加批次维度

    # 转换为PaddleTensor
    image_tensor = paddle.to_tensor(image)

    # 通过模型直接进行推理和输出
    with paddle.no_grad():
        output = model(image_tensor)
        prob = paddle.nn.functional.softmax(output, axis=1).numpy()
        predicted_class = np.argmax(prob, axis=1)[0]
        confidence = prob[0, predicted_class]

    return predicted_class

SEG_MODEL_PATH = 'E:/study/PycharmProjects/eyeseg/work_dirs/output/best_model/model.pdparams'
CLASSFICATION_MODEL_PATH = 'E:/study/PycharmProjects/eyeclassfication/work_dirs/output/best_model/model.pdparams'