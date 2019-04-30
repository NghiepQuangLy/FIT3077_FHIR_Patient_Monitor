# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogInView.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class UiLogIn(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.logInLabel = QtWidgets.QLabel(Form)
        self.logInLabel.setGeometry(QtCore.QRect(160, 80, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.logInLabel.setFont(font)
        self.logInLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logInLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logInLabel.setScaledContents(True)
        self.logInLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.logInLabel.setObjectName("logInLabel")
        self.submitButton = QtWidgets.QPushButton(Form)
        self.submitButton.setGeometry(QtCore.QRect(160, 190, 81, 23))
        self.submitButton.setObjectName("submitButton")
        self.enterIdLabel = QtWidgets.QLabel(Form)
        self.enterIdLabel.setGeometry(QtCore.QRect(60, 120, 71, 16))
        self.enterIdLabel.setObjectName("enterIdLabel")
        self.inputIdLineEdit = QtWidgets.QLineEdit(Form)
        self.inputIdLineEdit.setGeometry(QtCore.QRect(152, 120, 181, 20))
        self.inputIdLineEdit.setObjectName("inputIdLineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.logInLabel.setText(_translate("Form", "LOG IN"))
        self.submitButton.setText(_translate("Form", "Submit"))
        self.enterIdLabel.setText(_translate("Form", "Enter your ID:"))
