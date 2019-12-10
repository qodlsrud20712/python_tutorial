import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from chap_01 import chap01

class UserForm(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("userform.ui")
        self.ui.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = UserForm()
    sys.exit(app.exec())