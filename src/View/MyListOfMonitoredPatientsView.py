from PyQt5 import QtWidgets
from View.PyQt5GeneratedUis.ListOfPatientsView import UiListOfPatients
from Controller import MyListOfMonitoredPatientsViewController


class MyListOfMonitoredPatients(QtWidgets.QWidget):

    def __init__(self, controller: MyListOfMonitoredPatientsViewController):
        super().__init__()

        self._controller = controller
        self._ui = UiListOfPatients()
        self._ui.setupUi(self)
