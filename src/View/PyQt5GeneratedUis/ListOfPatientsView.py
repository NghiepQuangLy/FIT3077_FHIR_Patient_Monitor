# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListOfPatientsView.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class UiListOfPatients(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.allPatientListLabel = QtWidgets.QLabel(Form)
        self.allPatientListLabel.setGeometry(QtCore.QRect(10, 10, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.allPatientListLabel.setFont(font)
        self.allPatientListLabel.setObjectName("allPatientListLabel")
        self.allPatientListView = QtWidgets.QListView(Form)
        self.allPatientListView.setGeometry(QtCore.QRect(10, 40, 381, 192))
        self.allPatientListView.setModelColumn(0)
        self.allPatientListView.setObjectName("allPatientListView")
        self.allPatientListSortSelector = QtWidgets.QComboBox(Form)
        self.allPatientListSortSelector.setGeometry(QtCore.QRect(310, 10, 81, 22))
        self.allPatientListSortSelector.setObjectName("allPatientListSortSelector")
        self.allPatientListSortSelector.addItem("")
        self.showMonitoredPatientButton = QtWidgets.QPushButton(Form)
        self.showMonitoredPatientButton.setGeometry(QtCore.QRect(140, 240, 131, 23))
        self.showMonitoredPatientButton.setObjectName("showMonitoredPatientButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.allPatientListLabel.setText(_translate("Form", "LIST OF PATIENTS"))
        self.allPatientListSortSelector.setItemText(0, _translate("Form", "Cholesterol"))
        self.showMonitoredPatientButton.setText(_translate("Form", "Show Monitored Patients"))

