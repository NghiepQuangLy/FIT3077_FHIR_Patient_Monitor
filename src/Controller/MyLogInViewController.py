from PyQt5 import QtCore


class MyLogInViewController(QtCore.QObject):

    def __init__(self):
        super().__init__()

    @QtCore.pyqtSlot()
    def id_submitted(self, id: str):
        print(id)
        #self.finished.emit("my_list_of_patients_view")
