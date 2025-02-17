#!/usr/bin/python3
# author ekubo
# 2025年01月04日

from ui_changePWD import *
from config import USER_NOW, connect_database


class ChangePwdDialog(QDialog):
    def __init__(self, parent=None):
        super(ChangePwdDialog, self).__init__(parent)
        self.ui = Ui_Dialog_changePWD()
        self.ui.setupUi(self)
        self.setWindowTitle('修改密码')
        # 连接确认修改按钮的点击事件
        self.ui.pushButton.clicked.connect(self.changePwd)

    # 修改密码
    def changePwd(self):
        new_password = self.ui.lineEdit.text()
        confirm_password = self.ui.lineEdit_2.text()

        if not new_password or not confirm_password:
            self.ui.stackedWidget.setCurrentIndex(2)  # 显示文本"密码不能为空！"
            return

        if new_password != confirm_password:
            self.ui.stackedWidget.setCurrentIndex(1)  # 显示文本"两次输入的密码不一致！"
            return

        conn = connect_database()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE accounts SET password = %s WHERE account_name = %s", (new_password, USER_NOW.account_name))
            conn.commit()
            self.ui.stackedWidget.setCurrentIndex(3)  # 显示文本"密码修改成功！"
        except Exception as e:
            print(f"Error updating password: {e}")
        finally:
            conn.close()

