# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recordUI.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QTextBrowser, QVBoxLayout, QWidget)
import rcc_resource

class Ui_RecordWindow(object):
    def setupUi(self, RecordWindow):
        if not RecordWindow.objectName():
            RecordWindow.setObjectName(u"RecordWindow")
        RecordWindow.resize(1258, 827)
        self.centralwidget = QWidget(RecordWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 30, 1200, 756))
        self.widget.setMinimumSize(QSize(1200, 756))
        self.widget.setStyleSheet(u"background-color: rgb(25,35,45);")
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
        self.horizontalLayout = QHBoxLayout(self.frame_title)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_title)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.button_return = QPushButton(self.frame)
        self.button_return.setObjectName(u"button_return")
        icon = QIcon()
        icon.addFile(u":/images/images/UI/\u8fd4\u56de.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_return.setIcon(icon)
        self.button_return.setIconSize(QSize(20, 20))

        self.verticalLayout_10.addWidget(self.button_return)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(24)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"border-top-right-radius:0px;")

        self.horizontalLayout.addWidget(self.label_title)

        self.frame_2 = QFrame(self.frame_title)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(3)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_logout = QPushButton(self.frame_2)
        self.button_logout.setObjectName(u"button_logout")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/UI/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_logout.setIcon(icon1)
        self.button_logout.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.button_logout)

        self.button_small = QPushButton(self.frame_2)
        self.button_small.setObjectName(u"button_small")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/UI/small.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_small.setIcon(icon2)
        self.button_small.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.button_small)

        self.button_close = QPushButton(self.frame_2)
        self.button_close.setObjectName(u"button_close")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/UI/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_close.setIcon(icon3)
        self.button_close.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.button_close)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame_title)

        self.frame_main = QFrame(self.widget)
        self.frame_main.setObjectName(u"frame_main")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(15)
        sizePolicy4.setHeightForWidth(self.frame_main.sizePolicy().hasHeightForWidth())
        self.frame_main.setSizePolicy(sizePolicy4)
        self.frame_main.setStyleSheet(u"QFrame{\n"
"	border:1px solid rgb(90,120,140);\n"
"	border-radius:5px;\n"
"}\n"
"QGroupBox{\n"
"	border:1px solid rgb(90,120,140);\n"
"	border-radius:5px;\n"
"    color: white; /* \u8bbe\u7f6e\u6807\u9898\u5b57\u4f53\u989c\u8272\u4e3a\u767d\u8272 */\n"
"    font-size: 12px; /* \u4fee\u6539\u5b57\u4f53\u5927\u5c0f */\n"
"    font-weight: bold; /* \u8bbe\u7f6e\u5b57\u4f53\u52a0\u7c97 */\n"
"}\n"
"")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        sizePolicy.setHeightForWidth(self.frame_top.sizePolicy().hasHeightForWidth())
        self.frame_top.setSizePolicy(sizePolicy)
        self.frame_top.setStyleSheet(u"")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, -1, -1, -1)
        self.groupBox = QGroupBox(self.frame_top)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 14, -1, -1)
        self.calendarWidget = QCalendarWidget(self.groupBox)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setStyleSheet(u"background-color: rgb(220, 220, 220);")

        self.verticalLayout_3.addWidget(self.calendarWidget)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_top)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, 14, 3, -1)
        self.tableWidget = QTableWidget(self.groupBox_2)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        font1 = QFont()
        font1.setPointSize(9)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        font2 = QFont()
        self.tableWidget.setFont(font2)
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"        color: #ffffff;\n"
"        gridline-color: #444444;\n"
"        font-size: 10px;\n"
"    }\n"
"    QTableWidget::item {\n"
"        padding: 2px;\n"
"        border: none;\n"
"	   min-height:100px;\n"
"	   min-width:100px;\n"
"    }\n"
"    QHeaderView::section {\n"
"        background-color: rgb(70,80,102);\n"
"        color: #ffffff;\n"
"        border: 1px solid #444444;\n"
"        padding: 4px;\n"
"    }\n"
"    QTableWidget::item:selected {\n"
"        background-color: #505050;\n"
"    }")

        self.verticalLayout_5.addWidget(self.tableWidget)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame_top)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(15, 14, 15, 0)
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border:none;")

        self.verticalLayout_6.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.groupBox_3)


        self.verticalLayout_2.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.frame_main)
        self.frame_bottom.setObjectName(u"frame_bottom")
        sizePolicy.setHeightForWidth(self.frame_bottom.sizePolicy().hasHeightForWidth())
        self.frame_bottom.setSizePolicy(sizePolicy)
        self.frame_bottom.setStyleSheet(u"")
        self.frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_4 = QGroupBox(self.frame_bottom)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 14, -1, -1)
        self.textBrowser = QTextBrowser(self.groupBox_4)
        self.textBrowser.setObjectName(u"textBrowser")
        font3 = QFont()
        font3.setPointSize(13)
        self.textBrowser.setFont(font3)
        self.textBrowser.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.textBrowser)


        self.horizontalLayout_4.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.frame_bottom)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy1.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy1)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(15, 14, 15, 0)
        self.label_2 = QLabel(self.groupBox_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"border:none;")

        self.verticalLayout_7.addWidget(self.label_2)


        self.horizontalLayout_4.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.frame_bottom)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy1.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy1)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(15, 14, 15, 0)
        self.label_3 = QLabel(self.groupBox_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border:none;")

        self.verticalLayout_8.addWidget(self.label_3)


        self.horizontalLayout_4.addWidget(self.groupBox_6)


        self.verticalLayout_2.addWidget(self.frame_bottom)


        self.verticalLayout.addWidget(self.frame_main)

        RecordWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RecordWindow)
        self.button_close.clicked.connect(RecordWindow.close)
        self.button_small.clicked.connect(RecordWindow.showMinimized)

        QMetaObject.connectSlotsByName(RecordWindow)
    # setupUi

    def retranslateUi(self, RecordWindow):
        RecordWindow.setWindowTitle(QCoreApplication.translate("RecordWindow", u"MainWindow", None))
        self.button_return.setText("")
        self.label_title.setText(QCoreApplication.translate("RecordWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">\u8bca\u65ad\u8bb0\u5f55</span></p></body></html>", None))
        self.button_logout.setText("")
        self.button_small.setText("")
        self.button_close.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("RecordWindow", u"\u9009\u62e9\u65e5\u671f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("RecordWindow", u"\u5386\u53f2\u8bb0\u5f55", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("RecordWindow", u"\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("RecordWindow", u"\u8bca\u65ad\u7ed3\u679c", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("RecordWindow", u"\u8bca\u65ad\u65f6\u95f4", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("RecordWindow", u"\u539f\u56fe\u8def\u5f84", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("RecordWindow", u"\u6807\u7b7e\u56fe\u8def\u5f84", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("RecordWindow", u"\u539f\u52a0\u5206\u5272\u56fe\u8def\u5f84", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("RecordWindow", u"\u75c5\u7406\u4fe1\u606f", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("RecordWindow", u"\u539f\u56fe", None))
        self.label.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("RecordWindow", u"\u75c5\u7406\u4fe1\u606f", None))
        self.textBrowser.setHtml(QCoreApplication.translate("RecordWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("RecordWindow", u"\u89c6\u76d8\u89c6\u676f\u5206\u5272\u56fe", None))
        self.label_2.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("RecordWindow", u"\u539f\u56fe+\u5206\u5272\u56fe", None))
        self.label_3.setText("")
    # retranslateUi

