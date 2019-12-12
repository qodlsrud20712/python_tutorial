import sys

from PyQt5 import QtWidgets

from erp.department import MyErp

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MyErp()
    sys.exit(app.exec())
