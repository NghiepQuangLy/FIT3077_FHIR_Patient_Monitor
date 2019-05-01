from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from View.PyQt5GeneratedUis.LogInView import UiLogIn
from Controller import MyLogInViewController


class MyLogIn(QtWidgets.QWidget):

    def __init__(self, controller: MyLogInViewController):
        super().__init__()

        self._controller = controller
        self._ui = UiLogIn()
        self._ui.setupUi(self)

        self._ui.submitButton.clicked.connect(self.submit)
        self._controller.log_in_finished.connect(self.hide)

    @pyqtSlot()
    def submit(self):
        self._controller.id_submitted(self._ui.inputIdLineEdit.text())
