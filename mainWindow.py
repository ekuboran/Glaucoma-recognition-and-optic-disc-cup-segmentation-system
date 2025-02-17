#!/usr/bin/python3
# author ekubo
# 2025年01月03日

import os
import time
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui_diagnosisUI import *
from window.changePwd import ChangePwdDialog
from window.loginWindow import LoginWindow
from window.recordWindow import RecordWindow
from window.saveHint import SaveHintDialog

import cv2


# 分割任务线程
class SegmentationThread(QThread):
    update_message = Signal(str)        # Signal是pyside6提供的一种信号机制，用于在不同对象之间传递信息。它允许在一个对象中发出信号，并在另一个对象中捕获并处理信号。

    def __init__(self, resourceImg, output_size, parent=None):
        super(SegmentationThread, self).__init__(parent)
        self.resourceImg = resourceImg
        self.output_size = output_size

    def run(self):
        self.update_message.emit("正在执行视盘视杯分割，请稍等...")
        if self.parent().gRecord is None:
            self.parent().gRecord = config.GlaucomaRecord(record_time=datetime.now())         # 记录第一次诊断的时间
        self.parent().seg_model = config.seg_model_load(model_path=config.SEG_MODEL_PATH)
        result, result1, ratio = config.get_seg_result(self.parent().seg_model, img_path=self.resourceImg)    # 获取预测结果
        resize_scale = self.output_size / result.shape[0]                                      # 获取缩放比例
        # 将图片进行缩放
        im0 = cv2.resize(result, (0, 0), fx=resize_scale, fy=resize_scale)
        im1 = cv2.resize(result1, (0, 0), fx=resize_scale, fy=resize_scale)
        # 保存图片
        cv2.imwrite("E:/test/tmp_img/mask_img.jpg", im0)
        cv2.imwrite("E:/test/tmp_img/seg_img.jpg", im1)
        # 根据选中的单选按钮展示结果图
        if self.parent().ui.rbutton_op1.isChecked():
            self.parent().ui.label_bigImage.setPixmap(QPixmap("E:/test/tmp_img/mask_img.jpg"))
        elif self.parent().ui.rbutton_op2.isChecked():
            self.parent().ui.label_bigImage.setPixmap(QPixmap("E:/test/tmp_img/seg_img.jpg"))

        # 显示杯盘比病理信息
        result_txt = f"视盘视杯分割已完成。\n当前眼底图像的杯盘比为{ratio}, 安全阈值为0.45。\n"
        if ratio < 0.45:
            result_txt = result_txt + "温馨提示: 正常情况下，杯盘比大约在0.3左右。杯盘比低于安全阈值也可能患青光眼，需进行排青检查才能确定。"
        else:
            result_txt = result_txt + "温馨提示: 正常情况下，杯盘比大约在0.3左右。杯盘比增大不一定是青光眼，也可能是生理性杯盘比增大，需进行排青检查后才能确定。"
        self.parent().diagnosisMessage = "\n".join(result_txt.split("\n")[1:])
        self.update_message.emit(result_txt)


# 识别任务线程
class RecognizeThread(QThread):
    update_message = Signal(str)

    def __init__(self, parent=None):
        super(RecognizeThread, self).__init__(parent)
        # self.resourceImg = resourceImg

    def run(self) :
        self.update_message.emit("正在执行青光眼识别，请稍等...")
        if self.parent().gRecord is None:
            self.parent().gRecord = config.GlaucomaRecord(record_time=datetime.now())  # 记录第一次诊断的时间
        time.sleep(2)
        self.parent().recognizeFlag = 2
        self.parent().classfication_model = config.classfication_model_load(model_path=config.CLASSFICATION_MODEL_PATH)
        result = config.get_classfication_result(self.parent().classfication_model, img_path=self.resourceImg)
        if result == 0:
            self.update_message.emit("图像识别结果为：no-GON，即未患青光眼")
        else:
            self.update_message.emit("图像识别结果为：GON，即患有青光眼")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 设置窗口无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setupFileTreeView()  # 设置文件系统模型绑定
        self.ui.button_logout.clicked.connect(self.log_out)  # 设置退出登录按钮点击事件
        self.ui.button_changePwd.clicked.connect(self.open_change_pwd_dialog)  # 设置修改密码按钮点击事件
        self.ui.button_queryRecord.clicked.connect(self.open_recordWindow)  # 设置查询记录按钮点击事件
        self.ui.fileTreeView.clicked.connect(self.load_thumbnails_and_show_big_image)  # 添加树状文件夹点击事件处理
        self.ui.thumbnailListWidget.itemClicked.connect(self.show_big_image)  # 添加缩略图点击事件处理
        self.ui.rbutton_op1.setChecked(True)  # 设置"显示分割结果"按钮为默认选中状态
        # 设置分割任务两个按钮的点击事件处理
        self.ui.rbutton_op1.clicked.connect(self.change2maskimg)
        self.ui.rbutton_op2.clicked.connect(self.change2segimg)
        self.center_on_screen()  # 窗口居中

        # 分割/识别功能初始参数设置
        self.resourceImg = ""  # 设置检测原图的路径为空
        self.gRecord = None  # 设置记录对象的初始值为None
        self.recognizeFlag = 0  # 设置识别标志位为0 （0表示未识别，1表示识别结果为青光眼（GON）,2表示识别结果为正常（no-GON））
        self.diagnosisMessage = ''  # 设置病理信息初始值为空
        self.output_size = 559

        self.ui.button_seg.clicked.connect(self.diagnose)  # 设置视盘视杯分割按钮点击事件
        self.ui.button_recognize.clicked.connect(self.recognize)  # 设置青光眼识别按钮点击事件
        self.ui.button_saveRecord.clicked.connect(self.save_record)  # 设置保存记录按钮点击事件

        self.show()

    # 添加窗口居中显示的方法
    def center_on_screen(self):
        screen_geometry = QApplication.screenAt(QPoint()).geometry()
        x = (screen_geometry.width() - self.width()) / 2
        y = (screen_geometry.height() - self.height()) / 2
        self.move(x, y)

    # 拖动
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = self.m_Position = event.globalPosition().toPoint() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPosition().toPoint() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    # 退出登录
    def log_out(self):
        self.close()
        self.login = LoginWindow()
        config.USER_NOW = None

    # 打开修改密码对话框
    def open_change_pwd_dialog(self):
        self.change_pwd_dialog = ChangePwdDialog(self)
        self.change_pwd_dialog.show()

    # 打开查询记录窗口
    def open_recordWindow(self):
        self.close()
        self.recordWindow = RecordWindow()

    # 左侧文件系统绑定
    def setupFileTreeView(self):
        model = QFileSystemModel()
        model.setRootPath("")  # 设置根路径
        self.ui.fileTreeView.setModel(model)
        # 设置根索引
        root_index = model.index(model.rootPath())
        self.ui.fileTreeView.setRootIndex(root_index)
        # 展开到第2层
        self.ui.fileTreeView.expandToDepth(1)
        # 隐藏顶部字段名
        self.ui.fileTreeView.header().setVisible(False)
        # 只显示文件夹的名字，不显示size等其他属性
        self.ui.fileTreeView.setHeaderHidden(True)  # 隐藏所有列标题
        self.ui.fileTreeView.setColumnHidden(1, True)  # 隐藏大小列
        self.ui.fileTreeView.setColumnHidden(2, True)  # 隐藏类型列
        self.ui.fileTreeView.setColumnHidden(3, True)  # 隐藏修改日期列
        # 添加文件树点击事件处理
        self.ui.fileTreeView.doubleClicked.connect(self.show_big_image_from_tree)

    # 加载缩略图并显示大图
    def load_thumbnails_and_show_big_image(self, index):
        model = self.ui.fileTreeView.model()
        path = model.filePath(index)
        if os.path.isdir(path):
            self.ui.thumbnailListWidget.clear()
            for file_name in QDir(path).entryList(['*.png', '*.jpg', '*.jpeg', '*.bmp']):
                file_path = os.path.join(path, file_name)
                pixmap = QPixmap(file_path).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                item = QListWidgetItem(QIcon(pixmap), file_name)
                self.ui.thumbnailListWidget.addItem(item)
        # 如果选中的是文件夹，尝试显示第一个缩略图
        if self.ui.thumbnailListWidget.count() > 0:
            self.ui.thumbnailListWidget.setCurrentRow(0)
            self.show_big_image(self.ui.thumbnailListWidget.item(0))

    # 显示大图
    def show_big_image(self, item):
        file_name = item.text()
        model = self.ui.fileTreeView.model()
        path = model.filePath(self.ui.fileTreeView.currentIndex())
        file_path = os.path.join(path, file_name)
        self.display_big_image(file_path)

    # 从文件树中显示大图
    def show_big_image_from_tree(self, index):
        model = self.ui.fileTreeView.model()
        file_path = model.filePath(index)
        if os.path.isfile(file_path) and file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            self.display_big_image(file_path)

    # 显示大图的公共方法
    def display_big_image(self, file_path):
        pixmap = QPixmap(file_path)
        # 获取 QLabel 的大小
        label_size = self.ui.label_bigImage.size()
        # 缩放 pixmap 以适应 QLabel 的大小，保持宽高比
        scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        # 设置缩放后的 pixmap 到 QLabel
        self.ui.label_bigImage.setPixmap(scaled_pixmap)
        # 确保内容不会自动缩放
        self.ui.label_bigImage.setScaledContents(False)
        # 每次重置大图后重置记录对象和检测原图路径
        self.gRecord = None
        self.resourceImg = file_path

    # 分割
    def diagnose(self):
        # 另启动一个线程完成分割任务让更新UI线程不会被分割任务阻塞
        self.segmentation_thread = SegmentationThread(self.resourceImg, self.output_size, self)
        self.segmentation_thread.update_message.connect(self.ui.text_segMessage.setText)
        self.segmentation_thread.start()

    # 识别青光眼
    def recognize(self):
        # 另启一个线程完成识别任务让更新UI线程不会被识别任务阻塞
        self.segmentation_thread = RecognizeThread(self)
        self.segmentation_thread.update_message.connect(self.ui.text_recognizeResult.setText)
        self.segmentation_thread.start()

    # 保存记录
    def save_record(self):
        self.save_hint_dialog = SaveHintDialog(self)
        # 如果没有进行分割或者识别，则提示用户
        if self.gRecord is None or self.recognizeFlag == 0 or self.diagnosisMessage == "":
            self.save_hint_dialog.ui.stackedWidget.setCurrentIndex(0)
        # 如果已经进行了分割和识别，则提示成功并保存记录
        else:
            # 1.从数据库中读取最后一条记录的record_id
            engine = create_engine('mysql+pymysql://root:123@192.168.37.128:3307/glu_diag_sys')
            Session = sessionmaker(bind=engine)
            session = Session()
            last_record = session.query(config.GlaucomaRecord).order_by(config.GlaucomaRecord.record_id.desc()).first()
            new_id = last_record.record_id + 1 if last_record else 1
            session.close()

            # 2.将原图/标签图/分割图重命名为id+1.jpg并保存到对应文件夹
            original_img_path = f"E:/test/resource_img/{new_id}.jpg"
            mask_img_path = f"E:/test/mask_img/{new_id}.jpg"
            seg_img_path = f"E:/test/resourcewithseg_img/{new_id}.jpg"
            os.rename(self.resourceImg, original_img_path)
            os.rename("E:/test/tmp_img/mask_img.jpg", mask_img_path)
            os.rename("E:/test/tmp_img/seg_img.jpg", seg_img_path)

            # 3.将对应字段复制给gRecord
            self.gRecord.record_result = "GON" if self.recognizeFlag == 1 else "non-GON"
            self.gRecord.resource_img_address = original_img_path
            self.gRecord.result1_img_address = mask_img_path
            self.gRecord.result2_img_address = seg_img_path
            self.gRecord.message = self.diagnosisMessage

            # 4.通过orm将记录保存到数据库
            engine = create_engine('mysql+pymysql://root:123@192.168.37.128:3307/glu_diag_sys')
            Session = sessionmaker(bind=engine)
            session = Session()
            session.add(self.gRecord)
            session.commit()
            session.close()
            self.save_hint_dialog.ui.stackedWidget.setCurrentIndex(1)

        self.save_hint_dialog.show()

    # 通过单选按钮切换大图
    def change2maskimg(self):
        if self.gRecord is not None and self.diagnosisMessage != "":
            self.ui.label_bigImage.setPixmap(QPixmap("E:/test/tmp_img/mask_img.jpg"))

    def change2segimg(self):
        if self.gRecord is not None and self.diagnosisMessage != "":
            self.ui.label_bigImage.setPixmap(QPixmap("E:/test/tmp_img/seg_img.jpg"))