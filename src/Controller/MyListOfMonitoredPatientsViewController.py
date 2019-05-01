from PyQt5 import QtCore


class MyListOfMonitoredPatientsViewController(QtCore.QObject):

    list_of_monitored_patients_finished = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def show_all_patients(self):
        self.list_of_monitored_patients_finished.emit("list_of_patients")
