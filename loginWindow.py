#!/usr/bin/python3
# author ekubo
# 2025年01月03日
import time

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

import window.mainWindow
from ui_login import *
from ui_diagnosisUI import *
import pymysql
from config import USER_NOW, connect_database

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        # 设置窗口无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 设置登录注册按钮切换事件
        self.ui.pushButton_change2L.clicked.connect(self.change2Login)
        self.ui.pushButton_change2R.clicked.connect(self.change2Register)
        # 绑定登录的点击事件
        self.ui.loginButton.clicked.connect(self.login_in)
        # 绑定注册的点击事件
        self.ui.registerButton.clicked.connect(self.register_in)
        self.show()

    # 切换到登录页面
    def change2Login(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(5)
        self.ui.lineLoginUserName.clear()
        self.ui.lineLoginPassword.clear()

    # 切换到注册页面
    def change2Register(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
        self.ui.stackedWidget.setCurrentIndex(5)
        self.ui.lineRegisterUserName.clear()
        self.ui.lineRegisterPassword.clear()
        self.ui.lineRegisterPasswordAgain.clear()

    # 拖动
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = self.m_Position = event.globalPosition().toPoint() - self.pos()   # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPosition().toPoint() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    # 登录
    def login_in(self):
        username = self.ui.lineLoginUserName.text()
        password = self.ui.lineLoginPassword.text()
        
        # 清除之前的错误提示信息
        self.ui.stackedWidget.setCurrentIndex(5)
        if not username or not password:
            self.ui.stackedWidget.setCurrentIndex(4)  # 显示文本"账号或密码不能为空！"
            return
        
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts WHERE account_name = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            USER_NOW.account_name = username
            self.close()
            self.win = window.mainWindow.MainWindow()
        else:
            self.ui.stackedWidget.setCurrentIndex(0)  # 显示文本“账号不存在或密码错误！”

    # 注册
    def register_in(self):
        username = self.ui.lineRegisterUserName.text()
        password = self.ui.lineRegisterPassword.text()
        confirm_password = self.ui.lineRegisterPasswordAgain.text()
        
        if not username or not password or not confirm_password:
            self.ui.stackedWidget.setCurrentIndex(4)  # 显示文本"账号或密码不能为空！"
            return
        
        if password != confirm_password:
            self.ui.stackedWidget.setCurrentIndex(1)  # 显示文本"密码不一致！"
            return
        
        conn = connect_database()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM accounts WHERE account_name = %s", (username,))
            user = cursor.fetchone()
            if user:
                self.ui.stackedWidget.setCurrentIndex(2)  # 显示文本"该用户名已存在！"
                return
            
            cursor.execute("INSERT INTO accounts (account_name, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            self.ui.stackedWidget.setCurrentIndex(3)  # 显示文本"账号注册成功！"
        except pymysql.err.IntegrityError:
            self.ui.stackedWidget.setCurrentIndex(2)  # 显示文本"该用户名已存在！"
        finally:
            conn.close()

