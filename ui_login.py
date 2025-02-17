# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
import rcc_resource

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(1060, 695)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 180, 450, 450))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom-left-radius:30px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(570, 180, 450, 450))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius:30px;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 40, 900, 141))
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(39, 63, 156, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius:30px;\n"
"border-top-left-radius:30px;")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(970, 50, 35, 35))
        self.pushButton_4.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/images/images/UI/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(20, 20))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 210, 400, 400))
        self.label_4.setStyleSheet(u"border-image: url(:/images/images/UI/cdut_logo.png);\n"
"background-color: rgb(255, 255, 255);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(590, 200, 411, 421))
        self.frame.setMinimumSize(QSize(411, 421))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 9)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(5)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 0, 9, 0)
        self.stackedWidget_2 = QStackedWidget(self.frame_4)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(255, 255, 255,0);\n"
"	border:none;\n"
"	border-bottom:1px solid black;\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:7px;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-top:5px;\n"
"	padding-left:5px\n"
"}")
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.verticalLayout_5 = QVBoxLayout(self.page_login)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lineLoginUserName = QLineEdit(self.page_login)
        self.lineLoginUserName.setObjectName(u"lineLoginUserName")
        self.lineLoginUserName.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(13)
        self.lineLoginUserName.setFont(font)

        self.verticalLayout_5.addWidget(self.lineLoginUserName)

        self.lineLoginPassword = QLineEdit(self.page_login)
        self.lineLoginPassword.setObjectName(u"lineLoginPassword")
        self.lineLoginPassword.setMinimumSize(QSize(0, 40))
        self.lineLoginPassword.setFont(font)
        self.lineLoginPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_5.addWidget(self.lineLoginPassword)

        self.loginButton = QPushButton(self.page_login)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(11)
        self.loginButton.setFont(font1)

        self.verticalLayout_5.addWidget(self.loginButton)

        self.stackedWidget_2.addWidget(self.page_login)
        self.page_register = QWidget()
        self.page_register.setObjectName(u"page_register")
        self.verticalLayout_6 = QVBoxLayout(self.page_register)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lineRegisterUserName = QLineEdit(self.page_register)
        self.lineRegisterUserName.setObjectName(u"lineRegisterUserName")
        self.lineRegisterUserName.setMinimumSize(QSize(0, 40))
        self.lineRegisterUserName.setFont(font)

        self.verticalLayout_6.addWidget(self.lineRegisterUserName)

        self.lineRegisterPassword = QLineEdit(self.page_register)
        self.lineRegisterPassword.setObjectName(u"lineRegisterPassword")
        self.lineRegisterPassword.setMinimumSize(QSize(0, 40))
        self.lineRegisterPassword.setFont(font)
        self.lineRegisterPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_6.addWidget(self.lineRegisterPassword)

        self.lineRegisterPasswordAgain = QLineEdit(self.page_register)
        self.lineRegisterPasswordAgain.setObjectName(u"lineRegisterPasswordAgain")
        self.lineRegisterPasswordAgain.setMinimumSize(QSize(0, 40))
        self.lineRegisterPasswordAgain.setFont(font)
        self.lineRegisterPasswordAgain.setEchoMode(QLineEdit.Password)

        self.verticalLayout_6.addWidget(self.lineRegisterPasswordAgain)

        self.registerButton = QPushButton(self.page_register)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setMinimumSize(QSize(0, 40))

        self.verticalLayout_6.addWidget(self.registerButton)

        self.stackedWidget_2.addWidget(self.page_register)

        self.verticalLayout_4.addWidget(self.stackedWidget_2)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-top:5px;\n"
"	padding-left:5px\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_change2L = QPushButton(self.frame_5)
        self.pushButton_change2L.setObjectName(u"pushButton_change2L")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_change2L.sizePolicy().hasHeightForWidth())
        self.pushButton_change2L.setSizePolicy(sizePolicy3)
        self.pushButton_change2L.setSizeIncrement(QSize(100, 0))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/UI/login.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_change2L.setIcon(icon1)
        self.pushButton_change2L.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_change2L)

        self.pushButton_change2R = QPushButton(self.frame_5)
        self.pushButton_change2R.setObjectName(u"pushButton_change2R")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/UI/register.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_change2R.setIcon(icon2)
        self.pushButton_change2R.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_change2R)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_7 = QVBoxLayout(self.page_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_6.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_9 = QVBoxLayout(self.page_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_10 = QVBoxLayout(self.page_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_8 = QLabel(self.page_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_10.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_11 = QVBoxLayout(self.page_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_9 = QLabel(self.page_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_6)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_3)

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        self.pushButton_4.clicked.connect(LoginWindow.close)

        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:700; font-style:italic;\">\u9752\u5149\u773c\u8bc6\u522b\u4e0e\u89c6\u76d8\u89c6\u676f\u5206\u5272\u7cfb\u7edf</span></p></body></html>", None))
        self.pushButton_4.setText("")
        self.label_4.setText("")
        self.lineLoginUserName.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\u8d26\u53f7\uff1a", None))
        self.lineLoginPassword.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\u5bc6\u7801\uff1a", None))
        self.loginButton.setText(QCoreApplication.translate("LoginWindow", u"\u767b\u5f55", None))
        self.lineRegisterUserName.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\u8d26\u53f7\uff1a", None))
        self.lineRegisterPassword.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\u5bc6\u7801\uff1a", None))
        self.lineRegisterPasswordAgain.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\u786e\u8ba4\u5bc6\u7801\uff1a", None))
        self.registerButton.setText(QCoreApplication.translate("LoginWindow", u"\u6ce8\u518c", None))
        self.pushButton_change2L.setText("")
        self.pushButton_change2R.setText("")
        self.label_6.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" color:#ff0000;\">\u8d26\u53f7\u4e0d\u5b58\u5728\u6216\u5bc6\u7801\u9519\u8bef\uff01</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" color:#ff0000;\">\u5bc6\u7801\u4e0d\u4e00\u81f4\uff01</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" color:#ff0000;\">\u8be5\u7528\u6237\u540d\u5df2\u5b58\u5728\uff01</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" color:#009649;\">\u8d26\u53f7\u6ce8\u518c\u6210\u529f\uff01</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" color:#ff0000;\">\u8d26\u53f7\u6216\u5bc6\u7801\u4e0d\u80fd\u4e3a\u7a7a\uff01</span></p></body></html>", None))
    # retranslateUi

