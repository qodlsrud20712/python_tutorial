import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from chap_01 import chap01

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("chap01.ui")
        self.ui.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MyApp()
    sys.exit(app.exec())
    #
    # app = QApplication(sys.argv)
    # MainWindow = QMainWindow()
    # ui = chap01.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())