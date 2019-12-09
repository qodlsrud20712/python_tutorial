# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chap_01.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(908, 763)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.red_slider = QtWidgets.QSlider(Form)
        self.red_slider.setMaximum(255)
        self.red_slider.setOrientation(QtCore.Qt.Vertical)
        self.red_slider.setObjectName("red_slider")
        self.gridLayout.addWidget(self.red_slider, 2, 0, 1, 1)
        self.lbl_red = QtWidgets.QLabel(Form)
        self.lbl_red.setObjectName("lbl_red")
        self.gridLayout.addWidget(self.lbl_red, 0, 0, 1, 1)
        self.spin_red = QtWidgets.QSpinBox(Form)
        self.spin_red.setMaximum(255)
        self.spin_red.setObjectName("spin_red")
        self.gridLayout.addWidget(self.spin_red, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_green = QtWidgets.QLabel(Form)
        self.lbl_green.setObjectName("lbl_green")
        self.gridLayout_2.addWidget(self.lbl_green, 0, 0, 1, 1)
        self.spin_green = QtWidgets.QSpinBox(Form)
        self.spin_green.setMaximum(255)
        self.spin_green.setObjectName("spin_green")
        self.gridLayout_2.addWidget(self.spin_green, 1, 0, 1, 1)
        self.green_slider = QtWidgets.QSlider(Form)
        self.green_slider.setMaximum(255)
        self.green_slider.setOrientation(QtCore.Qt.Vertical)
        self.green_slider.setObjectName("green_slider")
        self.gridLayout_2.addWidget(self.green_slider, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbl_blue = QtWidgets.QLabel(Form)
        self.lbl_blue.setObjectName("lbl_blue")
        self.gridLayout_3.addWidget(self.lbl_blue, 0, 0, 1, 1)
        self.spin_blue = QtWidgets.QSpinBox(Form)
        self.spin_blue.setMaximum(255)
        self.spin_blue.setObjectName("spin_blue")
        self.gridLayout_3.addWidget(self.spin_blue, 1, 0, 1, 1)
        self.blue_slider = QtWidgets.QSlider(Form)
        self.blue_slider.setMaximum(255)
        self.blue_slider.setOrientation(QtCore.Qt.Vertical)
        self.blue_slider.setObjectName("blue_slider")
        self.gridLayout_3.addWidget(self.blue_slider, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)

        self.retranslateUi(Form)
        self.red_slider.valueChanged['int'].connect(self.spin_red.setValue)
        self.spin_red.valueChanged['int'].connect(self.red_slider.setValue)
        self.green_slider.valueChanged['int'].connect(self.spin_green.setValue)
        self.spin_green.valueChanged['int'].connect(self.green_slider.setValue)
        self.blue_slider.valueChanged['int'].connect(self.spin_blue.setValue)
        self.spin_blue.valueChanged['int'].connect(self.blue_slider.setValue)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_red.setText(_translate("Form", "RED"))
        self.lbl_green.setText(_translate("Form", "GREEN"))
        self.lbl_blue.setText(_translate("Form", "BLUE"))

