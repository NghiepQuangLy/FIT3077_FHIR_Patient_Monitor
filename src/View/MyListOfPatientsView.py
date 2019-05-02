from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from View.PyQt5GeneratedUis.ListOfPatientsView import UiListOfPatients
from Controller import MyListOfPatientsViewController


class MyListOfPatients(QtWidgets.QWidget):

    def __init__(self, controller: MyListOfPatientsViewController):
        super().__init__()

        self._controller = controller
        self._ui = UiListOfPatients()
        self._ui.setupUi(self)

        self._ui.showMonitoredPatientButton.clicked.connect(self.show_monitored_patients)
        self._controller.list_of_patients_finished.connect(self.hide)

    @pyqtSlot()
    def show_monitored_patients(self):
        self._controller.show_monitored_patients()

    def update(self, subject_state):
        print("hello")
