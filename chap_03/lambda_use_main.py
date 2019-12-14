import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget


class Lambda(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("lambda_use.ui")
        #lambda 함수를 이용한 버튼 클릭 두가지
        self.ui.btn_ok.clicked.connect(lambda state, button=self.ui.btn_ok: self.showLabel(state, button))
        #self.ui.btn_yes.clicked.connect(lambda state, button=self.ui.btn_yes: self.showLabel(state, button))

        #clicked는 bool값을 받는 매개변수를 선언해줘야되지만 pressed는 안 전해줘도 된다.
        self.ui.btn_yes.pressed.connect(lambda text=self.ui.btn_yes.text(): self.showLabelText(text))

        help(self.ui.lbl_res)
        self.ui.show()

    def showLabelText(self, text):
        self.ui.lbl_res.setText(text)

    def showLabel(self, state, button):
        message = button.text()
        self.ui.lbl_res.setText(message)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Lambda()
    sys.exit(app.exec())
