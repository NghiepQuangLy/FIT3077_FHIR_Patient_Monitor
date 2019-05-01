from PyQt5 import QtCore


class MyLogInViewController(QtCore.QObject):

    log_in_finished = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def id_submitted(self, id: str):
        print(id)
        self.log_in_finished.emit("list_of_patients")
        print("did emit maybe")

