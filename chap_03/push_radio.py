import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHeaderView


class PushRadioUI(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("push_radio_btns.ui")
        self.ui.btn_ok.clicked.connect(self.okclick)
        self.ui.btn_cancel.clicked.connect(self.cancelclick)
        self.ui.rb_male.clicked.connect(self.maleclick)
        self.ui.rb_female.clicked.connect(self.femaleclick)
        self.tbl_widget = self.ui.table_widget
        self.tbl_widget.setItem(0, 0, QTableWidgetItem('cell(0,0)'))
        item = QTableWidgetItem('cell(0,1)')
        item.setTextAlignment(Qt.AlignCenter)
        self.tbl_widget.setItem(0, 1, item)
        item1 = QTableWidgetItem('cell(0,2)')
        item1.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.tbl_widget.setItem(0, 2, item1)
        table_header = ['첫번째', '두번째', '세번째']
        self.tbl_widget.setHorizontalHeaderLabels(table_header)
        # row단위선택
        self.tbl_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 수정불가
        self.tbl_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.ui.btn_input.clicked.connect(self.input_tbl_item)
        self.ui.btn_delete.clicked.connect(self.delete_tbl_item)

        # 균일한간격으로
        self.tbl_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.show()

    def okclick(self):
        self.ui.lbl_push_res.setText(self.ui.btn_ok.text())

    def cancelclick(self):
        self.ui.lbl_push_res.setText(self.ui.btn_cancel.text())

    def maleclick(self):
        self.ui.lbl_rb_res.setText(self.ui.rb_male.text())

    def femaleclick(self):
        self.ui.lbl_rb_res.setText(self.ui.rb_female.text())

    def input_tbl_item(self):
        item = QTableWidgetItem('cell(1,1)')
        item.setTextAlignment(Qt.AlignCenter)
        currentRowCount = self.tbl_widget.rowCount()
        print(currentRowCount)
        self.tbl_widget.insertRow(currentRowCount)
        v1 = self.ui.le_01.text()
        v2 = self.ui.le_02.text()
        v3 = self.ui.le_03.text()
        item01 = QTableWidgetItem(v1)
        item01.setTextAlignment(Qt.AlignCenter)
        print(v1)
        self.tbl_widget.setItem(currentRowCount, 0, item01)
        self.tbl_widget.setItem(currentRowCount, 1, QTableWidgetItem(v2))
        self.tbl_widget.setItem(currentRowCount, 2, QTableWidgetItem(v3))

    def delete_tbl_item(self):
        selectionIdxs = self.tbl_widget.selectedIndexes()[0]
        print(selectionIdxs.row(), '', selectionIdxs.column())
        self.tbl_widget.removeRow(selectionIdxs.row())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = PushRadioUI()
    sys.exit(app.exec())
