# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListOfPatientsView.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 240, 131, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listView_3 = QtWidgets.QListView(Form)
        self.listView_3.setGeometry(QtCore.QRect(10, 40, 381, 192))
        self.listView_3.setModelColumn(0)
        self.listView_3.setObjectName("listView_3")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(310, 10, 81, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "LIST OF PATIENTS"))
        self.pushButton_3.setText(_translate("Form", "Show All Patients"))
        self.comboBox_2.setItemText(0, _translate("Form", "Cholesterol"))

