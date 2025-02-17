#!/usr/bin/python3
# author ekubo
# 2025年01月14日

from ui_saveHintUI import *

class SaveHintDialog(QDialog):
    def __init__(self, parent=None):
        super(SaveHintDialog, self).__init__(parent)
        self.ui = Ui_saveHintDialog()
        self.ui.setupUi(self)
        self.setWindowTitle('提示')
