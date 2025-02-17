# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diagnosisUI.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QTextEdit, QTreeView, QVBoxLayout,
    QWidget)
import rcc_resource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1197, 986)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 1150, 900))
        self.widget.setMinimumSize(QSize(1000, 770))
        self.widget.setStyleSheet(u"background-color: rgb(25, 35, 45);\n"
"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.widget)
        self.frame_title.setObjectName(u"frame_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy)
        self.frame_title.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(39, 63, 156, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(5)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"border-top-right-radius:0px;")

        self.horizontalLayout_2.addWidget(self.label_title)

        self.frame_close = QFrame(self.frame_title)
        self.frame_close.setObjectName(u"frame_close")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_close.sizePolicy().hasHeightForWidth())
        self.frame_close.setSizePolicy(sizePolicy2)
        self.frame_close.setStyleSheet(u"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"QPushButton{\n"
"	\n"
"	background-color: rgba(255, 255, 255,0);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover{\n"
"	padding-bottom:5px\n"
"}\n"
"")
        self.frame_close.setFrameShape(QFrame.StyledPanel)
        self.frame_close.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_close)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_logout = QPushButton(self.frame_close)
        self.button_logout.setObjectName(u"button_logout")
        icon = QIcon()
        icon.addFile(u":/images/images/UI/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_logout.setIcon(icon)
        self.button_logout.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.button_logout)

        self.button_small = QPushButton(self.frame_close)
        self.button_small.setObjectName(u"button_small")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/UI/small.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_small.setIcon(icon1)
        self.button_small.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.button_small)

        self.button_close = QPushButton(self.frame_close)
        self.button_close.setObjectName(u"button_close")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/UI/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_close.setIcon(icon2)
        self.button_close.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.button_close)


        self.horizontalLayout_2.addWidget(self.frame_close)


        self.verticalLayout.addWidget(self.frame_title)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(20)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setStyleSheet(u"QFrame{\n"
"	border:2px solid black;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 0, 3, 0)
        self.leftFrame = QFrame(self.frame)
        self.leftFrame.setObjectName(u"leftFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.leftFrame.sizePolicy().hasHeightForWidth())
        self.leftFrame.setSizePolicy(sizePolicy4)
        self.leftFrame.setFrameShape(QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftFrame)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 2, 1, 2)
        self.label_selectFile = QLabel(self.leftFrame)
        self.label_selectFile.setObjectName(u"label_selectFile")
        self.label_selectFile.setStyleSheet(u"border:none;")

        self.verticalLayout_2.addWidget(self.label_selectFile)

        self.fileTreeView = QTreeView(self.leftFrame)
        self.fileTreeView.setObjectName(u"fileTreeView")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.fileTreeView.sizePolicy().hasHeightForWidth())
        self.fileTreeView.setSizePolicy(sizePolicy5)
        self.fileTreeView.setStyleSheet(u"QTreeView::item {\n"
"    color: white;\n"
"}")

        self.verticalLayout_2.addWidget(self.fileTreeView)


        self.horizontalLayout.addWidget(self.leftFrame)

        self.midFrame = QFrame(self.frame)
        self.midFrame.setObjectName(u"midFrame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(3)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.midFrame.sizePolicy().hasHeightForWidth())
        self.midFrame.setSizePolicy(sizePolicy6)
        self.midFrame.setFrameShape(QFrame.StyledPanel)
        self.midFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.midFrame)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(12, 2, 12, 2)
        self.label_bigShow = QLabel(self.midFrame)
        self.label_bigShow.setObjectName(u"label_bigShow")
        sizePolicy.setHeightForWidth(self.label_bigShow.sizePolicy().hasHeightForWidth())
        self.label_bigShow.setSizePolicy(sizePolicy)
        self.label_bigShow.setStyleSheet(u"border:none;")

        self.verticalLayout_3.addWidget(self.label_bigShow)

        self.label_bigImage = QLabel(self.midFrame)
        self.label_bigImage.setObjectName(u"label_bigImage")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(45)
        sizePolicy7.setHeightForWidth(self.label_bigImage.sizePolicy().hasHeightForWidth())
        self.label_bigImage.setSizePolicy(sizePolicy7)
        self.label_bigImage.setMinimumSize(QSize(0, 0))
        self.label_bigImage.setStyleSheet(u"border:none;")
        self.label_bigImage.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label_bigImage)

        self.label_selectImage = QLabel(self.midFrame)
        self.label_selectImage.setObjectName(u"label_selectImage")
        sizePolicy.setHeightForWidth(self.label_selectImage.sizePolicy().hasHeightForWidth())
        self.label_selectImage.setSizePolicy(sizePolicy)
        self.label_selectImage.setStyleSheet(u"border:none;")

        self.verticalLayout_3.addWidget(self.label_selectImage)

        self.thumbnailListWidget = QListWidget(self.midFrame)
        self.thumbnailListWidget.setObjectName(u"thumbnailListWidget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(20)
        sizePolicy8.setHeightForWidth(self.thumbnailListWidget.sizePolicy().hasHeightForWidth())
        self.thumbnailListWidget.setSizePolicy(sizePolicy8)
        self.thumbnailListWidget.setStyleSheet(u"QListWidget::item {\n"
"                    color: white;\n"
"                }")
        self.thumbnailListWidget.setIconSize(QSize(100, 100))
        self.thumbnailListWidget.setViewMode(QListView.IconMode)

        self.verticalLayout_3.addWidget(self.thumbnailListWidget)


        self.horizontalLayout.addWidget(self.midFrame)

        self.rightFrame = QFrame(self.frame)
        self.rightFrame.setObjectName(u"rightFrame")
        sizePolicy4.setHeightForWidth(self.rightFrame.sizePolicy().hasHeightForWidth())
        self.rightFrame.setSizePolicy(sizePolicy4)
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.rightFrame)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.label_cdutLogo = QLabel(self.rightFrame)
        self.label_cdutLogo.setObjectName(u"label_cdutLogo")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(4)
        sizePolicy9.setHeightForWidth(self.label_cdutLogo.sizePolicy().hasHeightForWidth())
        self.label_cdutLogo.setSizePolicy(sizePolicy9)
        self.label_cdutLogo.setStyleSheet(u"border-image: url(:/images/images/UI/cdut_logo.png);\n"
"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_cdutLogo)

        self.frame_seg = QFrame(self.rightFrame)
        self.frame_seg.setObjectName(u"frame_seg")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(2)
        sizePolicy10.setHeightForWidth(self.frame_seg.sizePolicy().hasHeightForWidth())
        self.frame_seg.setSizePolicy(sizePolicy10)
        self.frame_seg.setFrameShape(QFrame.StyledPanel)
        self.frame_seg.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_seg)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 201, 111))
        self.segVerticalLayout = QVBoxLayout(self.layoutWidget)
        self.segVerticalLayout.setSpacing(0)
        self.segVerticalLayout.setObjectName(u"segVerticalLayout")
        self.segVerticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.segVerticalLayout.setContentsMargins(5, 0, 5, 0)
        self.button_seg = QPushButton(self.layoutWidget)
        self.button_seg.setObjectName(u"button_seg")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.button_seg.setFont(font1)
        self.button_seg.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(70, 83, 100);")
        self.button_seg.setIconSize(QSize(16, 16))

        self.segVerticalLayout.addWidget(self.button_seg)

        self.rbutton_op1 = QRadioButton(self.layoutWidget)
        self.rbutton_op1.setObjectName(u"rbutton_op1")
        font2 = QFont()
        font2.setPointSize(9)
        self.rbutton_op1.setFont(font2)
        self.rbutton_op1.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.segVerticalLayout.addWidget(self.rbutton_op1)

        self.rbutton_op2 = QRadioButton(self.layoutWidget)
        self.rbutton_op2.setObjectName(u"rbutton_op2")
        self.rbutton_op2.setFont(font2)
        self.rbutton_op2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.segVerticalLayout.addWidget(self.rbutton_op2)


        self.verticalLayout_4.addWidget(self.frame_seg)

        self.text_segMessage = QTextEdit(self.rightFrame)
        self.text_segMessage.setObjectName(u"text_segMessage")
        sizePolicy9.setHeightForWidth(self.text_segMessage.sizePolicy().hasHeightForWidth())
        self.text_segMessage.setSizePolicy(sizePolicy9)
        font3 = QFont()
        font3.setPointSize(10)
        self.text_segMessage.setFont(font3)
        self.text_segMessage.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.text_segMessage)

        self.text_recognizeResult = QTextEdit(self.rightFrame)
        self.text_recognizeResult.setObjectName(u"text_recognizeResult")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(2)
        sizePolicy11.setHeightForWidth(self.text_recognizeResult.sizePolicy().hasHeightForWidth())
        self.text_recognizeResult.setSizePolicy(sizePolicy11)
        self.text_recognizeResult.setFont(font3)
        self.text_recognizeResult.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.text_recognizeResult)

        self.frame_otherFeature = QFrame(self.rightFrame)
        self.frame_otherFeature.setObjectName(u"frame_otherFeature")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(3)
        sizePolicy12.setHeightForWidth(self.frame_otherFeature.sizePolicy().hasHeightForWidth())
        self.frame_otherFeature.setSizePolicy(sizePolicy12)
        self.frame_otherFeature.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(70,83,100);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.frame_otherFeature.setFrameShape(QFrame.StyledPanel)
        self.frame_otherFeature.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_otherFeature)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 0, 10, 0)
        self.button_recognize = QPushButton(self.frame_otherFeature)
        self.button_recognize.setObjectName(u"button_recognize")
        font4 = QFont()
        font4.setPointSize(11)
        self.button_recognize.setFont(font4)

        self.verticalLayout_5.addWidget(self.button_recognize)

        self.button_changePwd = QPushButton(self.frame_otherFeature)
        self.button_changePwd.setObjectName(u"button_changePwd")
        self.button_changePwd.setFont(font4)

        self.verticalLayout_5.addWidget(self.button_changePwd)

        self.button_saveRecord = QPushButton(self.frame_otherFeature)
        self.button_saveRecord.setObjectName(u"button_saveRecord")
        self.button_saveRecord.setFont(font4)

        self.verticalLayout_5.addWidget(self.button_saveRecord)

        self.button_queryRecord = QPushButton(self.frame_otherFeature)
        self.button_queryRecord.setObjectName(u"button_queryRecord")
        self.button_queryRecord.setFont(font4)

        self.verticalLayout_5.addWidget(self.button_queryRecord)


        self.verticalLayout_4.addWidget(self.frame_otherFeature)


        self.horizontalLayout.addWidget(self.rightFrame)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.button_close.clicked.connect(MainWindow.close)
        self.button_small.clicked.connect(MainWindow.showMinimized)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">\u9752\u5149\u773c\u8bc6\u522b\u4e0e\u89c6\u76d8\u89c6\u676f\u5206\u5272\u7cfb\u7edf</span></p></body></html>", None))
        self.button_logout.setText("")
        self.button_small.setText("")
        self.button_close.setText("")
        self.label_selectFile.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">\u6587\u4ef6\u9009\u62e9</span></p></body></html>", None))
        self.label_bigShow.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">\u5927\u56fe\u5c55\u793a</span></p></body></html>", None))
        self.label_bigImage.setText("")
        self.label_selectImage.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">\u56fe\u7247\u9009\u62e9</span></p></body></html>", None))
        self.label_cdutLogo.setText("")
        self.button_seg.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u76d8\u89c6\u676f\u5206\u5272", None))
        self.rbutton_op1.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u5206\u5272\u7ed3\u679c", None))
        self.rbutton_op2.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u5206\u5272\u533a\u57df", None))
        self.text_segMessage.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.button_recognize.setText(QCoreApplication.translate("MainWindow", u"\u9752\u5149\u773c\u8bc6\u522b", None))
        self.button_changePwd.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5bc6\u7801", None))
        self.button_saveRecord.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8bb0\u5f55", None))
        self.button_queryRecord.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u8bb0\u5f55", None))
    # retranslateUi

