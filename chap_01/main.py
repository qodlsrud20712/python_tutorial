import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from chap_01.chap01 import MyApp

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