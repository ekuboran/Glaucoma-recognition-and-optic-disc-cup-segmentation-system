# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'changePWD.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Dialog_changePWD(object):
    def setupUi(self, Dialog_changePWD):
        if not Dialog_changePWD.objectName():
            Dialog_changePWD.setObjectName(u"Dialog_changePWD")
        Dialog_changePWD.resize(404, 296)
        self.verticalLayout = QVBoxLayout(Dialog_changePWD)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.frame = QFrame(Dialog_changePWD)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(13, -1, 13, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"QLineEdit {\n"
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
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 40))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.lineEdit_2)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(11)
        self.pushButton.setFont(font1)

        self.verticalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_4 = QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_6.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_5 = QVBoxLayout(self.page_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.page_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_6 = QVBoxLayout(self.page_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_8 = QLabel(self.page_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog_changePWD)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog_changePWD)
    # setupUi

    def retranslateUi(self, Dialog_changePWD):
        Dialog_changePWD.setWindowTitle(QCoreApplication.translate("Dialog_changePWD", u"Dialog", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog_changePWD", u"\u5bc6\u7801\uff1a", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog_changePWD", u"\u786e\u8ba4\u5bc6\u7801\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog_changePWD", u"\u786e\u8ba4\u4fee\u6539", None))
        self.label_6.setText(QCoreApplication.translate("Dialog_changePWD", u"<html><head/><body><p><span style=\" color:#ff0000;\">\u4e24\u6b21\u8f93\u5165\u7684\u5bc6\u7801\u4e0d\u4e00\u81f4\uff01</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Dialog_changePWD", u"<html><head/><body><p><span style=\" color:#ff0000;\">\u5bc6\u7801\u4e0d\u80fd\u4e3a\u7a7a\uff01</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Dialog_changePWD", u"<html><head/><body><p><span style=\" color:#009649;\">\u5bc6\u7801\u4fee\u6539\u6210\u529f\uff01</span></p></body></html>", None))
    # retranslateUi

