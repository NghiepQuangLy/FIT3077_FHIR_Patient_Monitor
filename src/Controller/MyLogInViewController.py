from PyQt5.QtCore import pyqtSlot


class MyLogInViewController:

    @pyqtSlot()
    def id_submitted(self, id: str):
        print(id)

