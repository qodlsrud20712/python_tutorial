import sys
import typing

from PyQt5 import QtCore, uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from pyqt import hello_pyqt5

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("hello_pyqt5.ui")
        self.ui.show()


if __name__ == '__main__':
    # app = QtWidgets.QApplication(sys.argv)
    # w = MyApp()
    # sys.exit(app.exec())

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = hello_pyqt5.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())