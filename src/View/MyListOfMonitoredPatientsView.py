from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from View.PyQt5GeneratedUis.ListOfMonitoredPatientsView import UiListOfMonitoredPatients
from Controller import MyListOfMonitoredPatientsViewController


class MyListOfMonitoredPatients(QtWidgets.QWidget):

    def __init__(self, controller: MyListOfMonitoredPatientsViewController):
        super().__init__()

        self._controller = controller
        self._ui = UiListOfMonitoredPatients()
        self._ui.setupUi(self)

        self._ui.showAllPatientButton.clicked.connect(self.show_all_patients)
        self._controller.list_of_monitored_patients_finished.connect(self.hide)

    @pyqtSlot()
    def show_all_patients(self):
        self._controller.show_all_patients()
