import mmcv
import pymysql
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from mmseg.apis import inference_model, init_model, show_result_pyplot
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


# 模型加载
def model_load(model_path, config_path, device):
    # model = init_segmentor(config_path, model_path, device=DEVICE)
    model = init_model(config_path, model_path, device=device)
    # 添加模型信息
    model.dataset_meta['classes'] = ('background', 'Optic Cup', 'Optic Disc')
    # model.dataset_meta['palette'] = [[255, 255, 255], [128, 0, 0], [0, 128, 0]]             # 黑色、红色、绿色
    model.dataset_meta['palette'] = [[255, 255, 255], [0, 0, 0], [128, 128, 128]]  # 白色、黑色、灰色
    return model

def get_result(model, img_path):
    # 通过模型直接进行推理和输出
    result = inference_model(model, img_path)
    # 三类分割图
    vis_result1 = show_result_pyplot(model, img_path, result, show=False, out_file='demo/tmp/images_tmp.jpg',
                                    opacity=1, with_labels=False)

    # 构造带分割区域的原图
    # 从预测结果中提取分割图
    seg_map = result.pred_sem_seg.data.cpu().numpy().astype(np.uint8).squeeze()
    # 读取原图
    vis_result2 = mmcv.imread(img_path)
    # 绘制类别 1 的绿色轮廓
    seg_map_class1 = (seg_map == 1).astype(np.uint8)  # 提取类别 1 的二值图
    contours_class1, _ = cv2.findContours(seg_map_class1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(vis_result2, contours_class1, -1, (0, 255, 0), thickness=2)  # 设置轮廓颜色为绿色
    # 绘制类别 2 的蓝色轮廓
    seg_map_class2 = (seg_map == 2).astype(np.uint8)  # 提取类别 2 的二值图
    contours_class2, _ = cv2.findContours(seg_map_class2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(vis_result2, contours_class2, -1, (255, 0, 0), thickness=2)  # 设置轮廓颜色为蓝色  注：OpenCV的颜色通道默认是BGR的，所以这里设置轮廓颜色为蓝色

    # 通过像素点个数计算杯盘比
    result_copy = copy.deepcopy(result)
    numpy_data = result_copy.pred_sem_seg.numpy().data
    cup_count = np.sum(numpy_data == 1)
    disc_count = np.sum(numpy_data == 2)

    ratio = round(cup_count / (disc_count + cup_count), 5)

    return vis_result1, vis_result2, ratio

MODEL_PATH = 'E:/study/PycharmProjects/eyeseg/work_dirs/refuge-deeplabv3plus_r50-d8_4xb2-40k_512x512.pth'
CONFIG_PATH = 'E:/study/PycharmProjects/eyeseg/work_dirs/refuge-deeplabv3plus_r50-d8_4xb2-40k_512x512.py'
DEVICE = 'cuda:0'

