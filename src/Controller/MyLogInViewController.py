from PyQt5 import QtCore


class MyLogInViewController(QtCore.QObject):

    log_in_finished = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def id_submitted(self, id: str):
        self.log_in_finished.emit(id)
