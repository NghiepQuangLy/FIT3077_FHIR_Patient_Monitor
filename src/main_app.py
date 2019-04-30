import sys
from PyQt5 import QtWidgets, QtCore
from View.MyLogInView import MyLogIn
from View.MyListOfPatientsView import MyListOfPatients
from View.MyListOfMonitoredPatientsView import MyListOfMonitoredPatients
from Controller.MyLogInViewController import MyLogInViewController
from Controller.MyListOfPatientsViewController import MyListOfPatientsViewController
from Controller.MyListOfMonitoredPatientsViewController import MyListOfMonitoredPatientsViewController

class Application(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super(Application, self).__init__(sys_argv)
        self._views = {}

        log_in_view_controller = MyLogInViewController()
        self._views["log_in"] = MyLogIn(log_in_view_controller)

        list_of_patients_view_controller = MyListOfPatientsViewController()
        self._views["list_of_patients"] = MyListOfPatients(list_of_patients_view_controller)

        list_of_monitored_patients_view_controller = MyListOfMonitoredPatientsViewController()
        self._views["list_of_monitored_patients"] = MyListOfMonitoredPatients(list_of_monitored_patients_view_controller)

        self.change_view("log_in")

    @QtCore.pyqtSlot(str)
    def change_view(self, view_name):
        view = self._views.get(view_name)
        if view is not None:
            view.show()


if __name__ =='__main__':
    app = Application(sys.argv)
    sys.exit(app.exec())
