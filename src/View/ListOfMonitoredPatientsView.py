# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListOfMonitoredPatientsView.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.monitoredPatientListView = QtWidgets.QListView(Form)
        self.monitoredPatientListView.setGeometry(QtCore.QRect(10, 40, 381, 192))
        self.monitoredPatientListView.setModelColumn(0)
        self.monitoredPatientListView.setObjectName("monitoredPatientListView")
        self.monitoredPatientListTypeSelector = QtWidgets.QComboBox(Form)
        self.monitoredPatientListTypeSelector.setGeometry(QtCore.QRect(310, 10, 81, 22))
        self.monitoredPatientListTypeSelector.setObjectName("monitoredPatientListTypeSelector")
        self.monitoredPatientListTypeSelector.addItem("")
        self.showAllPatientButton = QtWidgets.QPushButton(Form)
        self.showAllPatientButton.setGeometry(QtCore.QRect(130, 240, 131, 23))
        self.showAllPatientButton.setObjectName("showAllPatientButton")
        self.monitoredPatientListLabel = QtWidgets.QLabel(Form)
        self.monitoredPatientListLabel.setGeometry(QtCore.QRect(10, 10, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.monitoredPatientListLabel.setFont(font)
        self.monitoredPatientListLabel.setObjectName("monitoredPatientListLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.monitoredPatientListTypeSelector.setItemText(0, _translate("Form", "Cholesterol"))
        self.showAllPatientButton.setText(_translate("Form", "Show All Patients"))
        self.monitoredPatientListLabel.setText(_translate("Form", "LIST OF PATIENTS"))

