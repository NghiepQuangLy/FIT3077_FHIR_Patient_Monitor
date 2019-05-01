from PyQt5 import QtWidgets
from View.PyQt5GeneratedUis.ListOfMonitoredPatientsView import UiListOfMonitoredPatients
from Controller import MyListOfMonitoredPatientsViewController


class MyListOfMonitoredPatients(QtWidgets.QWidget):

    def __init__(self, controller: MyListOfMonitoredPatientsViewController):
        super().__init__()

        self._controller = controller
        self._ui = UiListOfMonitoredPatients()
        self._ui.setupUi(self)
