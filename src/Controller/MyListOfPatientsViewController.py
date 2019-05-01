from PyQt5 import QtCore


class MyListOfPatientsViewController(QtCore.QObject):

    list_of_patients_finished = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def show_monitored_patients(self):
        self.list_of_patients_finished.emit("list_of_monitored_patients")
