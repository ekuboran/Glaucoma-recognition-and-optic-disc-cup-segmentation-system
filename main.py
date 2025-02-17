import sys
from loginWindow import *
from mainWindow import  *
from changePwd import *
from recordWindow import *
from saveHint import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    # win = MainWindow()
    # win = ChangePwdDialog()
    # win = RecordWindow()
    # win = SaveHintDialog()
    # win.show()
    sys.exit(app.exec())
