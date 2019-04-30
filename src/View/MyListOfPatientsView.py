from PyQt5 import QtWidgets
from View.PyQt5GeneratedUis.ListOfPatientsView import UiListOfPatients
from Controller import MyListOfPatientsViewController


class MyListOfPatients(QtWidgets.QWidget):

    def __init__(self, controller: MyListOfPatientsViewController):
        super().__init__()

        self._controller = controller
        self._ui = UiListOfPatients()
        self._ui.setupUi(self)
