# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'saveHintUI.ui'
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
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)
import rcc_resource

class Ui_saveHintDialog(object):
    def setupUi(self, saveHintDialog):
        if not saveHintDialog.objectName():
            saveHintDialog.setObjectName(u"saveHintDialog")
        saveHintDialog.resize(232, 89)
        self.verticalLayout = QVBoxLayout(saveHintDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(saveHintDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 0, 211, 61))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 10, 45, 45))
        self.label_3.setStyleSheet(u"image: url(:/images/images/UI/\u5931\u8d25-01.png);")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(53, 5, 161, 51))
        font = QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 45, 45))
        self.label.setStyleSheet(u"image: url(:/images/images/UI/\u6210\u529f.png);")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 20, 111, 31))
        self.label_2.setFont(font)
        self.stackedWidget.addWidget(self.page_2)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 55, 61, 25))
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"background-color: rgb(25,35,45);")

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(saveHintDialog)
        self.pushButton.clicked.connect(saveHintDialog.close)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(saveHintDialog)
    # setupUi

    def retranslateUi(self, saveHintDialog):
        saveHintDialog.setWindowTitle(QCoreApplication.translate("saveHintDialog", u"Dialog", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("saveHintDialog", u"<html><head/><body><p align=\"center\"><span style=\" color:#ff5500;\">\u4fdd\u5b58\u5931\u8d25\uff01<br/>\u60a8\u8fd8\u672a\u8fdb\u884c\u5206\u5272\u6216\u8bc6\u522b\uff01</span></p></body></html>", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("saveHintDialog", u"<html><head/><body><p align=\"center\">\u4fdd\u5b58\u6210\u529f\uff01</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("saveHintDialog", u"\u786e\u5b9a", None))
    # retranslateUi

