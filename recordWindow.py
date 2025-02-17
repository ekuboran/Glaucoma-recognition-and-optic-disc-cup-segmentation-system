#!/usr/bin/python3
# author ekubo
# 2025年01月10日

import os
import config

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import window.mainWindow
from ui_recordUI import *
from window.loginWindow import LoginWindow


# from window.mainWindow import MainWindow


class RecordWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RecordWindow()
        self.ui.setupUi(self)
        # 设置窗口无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.center_on_screen()  # 窗口居中
        self.ui.button_logout.clicked.connect(self.log_out)  # 设置退出登录按钮点击事件
        self.ui.button_return.clicked.connect(self.return_main)  # 设置返回按钮点击事件
        self.ui.calendarWidget.clicked.connect(self.load_records_for_date)  # 设置日期栏选择日期事件
        # 设置历史记录表格列宽
        self.ui.tableWidget.setColumnWidth(0, 45)
        self.ui.tableWidget.setColumnWidth(1, 65)
        self.ui.tableWidget.setColumnWidth(2, 110)
        self.ui.tableWidget.setColumnWidth(3, 145)
        self.ui.tableWidget.verticalHeader().setVisible(False)  # 隐藏行号
        self.ui.tableWidget.hideColumn(4)   # 隐藏第5列
        self.ui.tableWidget.hideColumn(5)   # 隐藏第6列
        self.ui.tableWidget.hideColumn(6)   # 隐藏第7列
        self.ui.tableWidget.hideColumn(7)   # 隐藏第8列
        self.ui.tableWidget.itemSelectionChanged.connect(self.load_data_for_record)   # 设置表格选择事件

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

    # 返回主界面
    def return_main(self):
        self.close()
        self.main = window.mainWindow.MainWindow()

    # 选中日期并加载诊断记录到右侧表格中
    def load_records_for_date(self, date):
        selected_date = date.toString("yyyy-MM-dd")  # 获取选择的日期
        # 从数据库中查询选中日期的诊断记录
        query = f"SELECT record_id, record_result, record_time, resource_img_address, result1_img_address, result2_img_address, message FROM glaucoma_records WHERE DATE(record_time)='{selected_date}'"
        records = self.execute_query(query)
        # 清空 QTableWidget 并重新加载数据
        self.ui.tableWidget.setRowCount(0)
        for record in records:
            row_position = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_position)
            for col, data in enumerate(record):
                item = QTableWidgetItem(str(data))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)        # 设置单元格不可编辑
                self.ui.tableWidget.setItem(row_position, col, item)

    # 执行数据库查询语句
    def execute_query(self, query):
        conn = config.connect_database()
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results

    # 加载选中记录的数据
    def load_data_for_record(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row == -1:
            return

        resource_image_path = self.ui.tableWidget.item(selected_row, 3).text()       # 获取原图的图片路径
        result1_image_path = self.ui.tableWidget.item(selected_row, 4).text()        # 获取标签图的图片路径
        result2_image_path = self.ui.tableWidget.item(selected_row, 5).text()        # 获取原图+分割的图片路径
        message = self.ui.tableWidget.item(selected_row, 6).text()

        # 加载图片
        original_image = QPixmap(resource_image_path)
        label_image_path = QPixmap(result1_image_path)
        segmented_image_path = QPixmap(result2_image_path)

        self.ui.label.setPixmap(original_image.scaled(self.ui.label.size(), Qt.KeepAspectRatio))
        self.ui.label_2.setPixmap(label_image_path.scaled(self.ui.label.size(), Qt.KeepAspectRatio))
        self.ui.label_3.setPixmap(segmented_image_path.scaled(self.ui.label.size(), Qt.KeepAspectRatio))
        self.ui.textBrowser.setText(message)

    # 从数据库中查询到对应记录后加载数据
    # def load_result_and_info(self):
    #     selected_row = self.tableWidget.currentRow()
    #     if selected_row == -1:
    #         return
    #     # 获取选中记录的 ID
    #     record_id = self.tableWidget.item(selected_row, 0).text()  # 假设第1列为 ID
    #     # 从数据库查询结果和详细信息
    #     query = f"SELECT result, details FROM diagnosis WHERE id={record_id}"
    #     result, details = self.execute_query(query)[0]
    #     # 显示结果
    #     self.listWidget_result.clear()
    #     self.listWidget_result.addItem(result)
    #     # 显示详细信息
    #     self.textBrowser_info.setText(details)
