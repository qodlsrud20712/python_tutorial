import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QHeaderView, QTableWidgetItem, QAction, QMessageBox


class Dept_form(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("deptform.ui")
        self.ui.tableWidget.setHorizontalHeaderLabels(['부서번호', '부서명', '위치'])
        # row단위선택
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 수정불가
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 균일 간격 재배치
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tbl_widget = self.ui.table_widget

        # slot/signal
        self.ui.btn_add.clicked.connect(self.add_item)
        self.ui.btn_update.clicked.connect(self.update_item)
        self.ui.btn_del.clicked.connect(self.del_item)
        self.ui.btn_init.clicked.connect(self.init_item)

        # 마우스 우클릭시 메뉴
        self.set_context_menu(self.ui.tableWidget)

        data = [(1, '마케팅', 8), (2, '개발', 10), (3, '인사', 20)]
        self.load_data(data)

        self.ui.show()

    def load_data(self, data):
        for idx, (no, name, floor) in enumerate(data):
            item_floor, item_name, item_no = self.create_item(floor, name, no)
            nextIdx = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(nextIdx)
            self.ui.tableWidget.setItem(nextIdx, 0, item_no)
            self.ui.tableWidget.setItem(nextIdx, 1, item_name)
            self.ui.tableWidget.setItem(nextIdx, 2, item_floor)

    def set_context_menu(self, tv):
        tv.setContextMenuPolicy(Qt.ActionsContextMenu)
        update_action = QAction('수정', tv)
        delete_action = QAction('삭제', tv)
        tv.addAction(update_action)
        tv.addAction(delete_action)
        update_action.triggered.connect(self.__update)
        delete_action.triggered.connect(self.__delete)

    def __update(self):
        item_no, item_name, item_floor = self.get_item_form_le()
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]
        # print(selectionIdxs.row())
        self.ui.tableWidget.setItem(selectionIdxs.row(), 0, item_no)
        self.ui.tableWidget.setItem(selectionIdxs.row(), 1, item_name)
        self.ui.tableWidget.setItem(selectionIdxs.row(), 2, item_floor)
        self.init_item()
        QMessageBox.information(self, 'Update', '확인', QMessageBox.Ok)

    def __delete(self):
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]
        self.ui.tableWidget.removeRow(selectionIdxs.row())
        QMessageBox.information(self, 'Delete', '확인', QMessageBox.Ok)

    def add_item(self):
        item_no, item_name, item_floor = self.get_item_form_le()
        currentIdx = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(currentIdx)
        self.ui.tableWidget.setItem(currentIdx, 0, item_no)
        self.ui.tableWidget.setItem(currentIdx, 1, item_name)
        self.ui.tableWidget.setItem(currentIdx, 2, item_floor)
        self.init_item()

    def get_item_form_le(self):
        no = self.ui.le_deptno.text()
        name = self.ui.le_deptname.text()
        floor = self.ui.le_floor.text()
        return self.create_item(floor, name, no)

    def create_item(self, floor, name, no):
        item_no = QTableWidgetItem()
        item_no.setTextAlignment(Qt.AlignCenter)
        item_no.setData(Qt.DisplayRole, no)
        item_name = QTableWidgetItem()
        item_name.setTextAlignment(Qt.AlignCenter)
        item_name.setData(Qt.DisplayRole, name)
        item_floor = QTableWidgetItem()
        item_floor.setTextAlignment(Qt.AlignCenter)
        item_floor.setData(Qt.DisplayRole, floor)
        return item_floor, item_name, item_no

    def update_item(self):
        item_no, item_name, item_floor = self.get_item_form_le()
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]
        # print(selectionIdxs.row())
        self.ui.tableWidget.setItem(selectionIdxs.row(), 0, item_no)
        self.ui.tableWidget.setItem(selectionIdxs.row(), 1, item_name)
        self.ui.tableWidget.setItem(selectionIdxs.row(), 2, item_floor)
        self.init_item()

    def del_item(self):
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]
        self.ui.tableWidget.removeRow(selectionIdxs.row())

    def init_item(self):
        self.ui.le_deptno.clear()
        self.ui.le_deptname.clear()
        self.ui.le_floor.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Dept_form()
    sys.exit(app.exec())
