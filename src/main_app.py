import sys
from PyQt5 import QtWidgets, QtCore
from DataModel.Model import Model
from WebDataAccess.FetchEngine import FetchEngine
from WebDataAccess.FhirApiFetcherProtocol import FhirApiFetcherProtocol
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
        self._controller = {}
        self._model = None

        log_in_view_controller = MyLogInViewController()
        self._views["log_in"] = MyLogIn(log_in_view_controller)

        self._controller["log_in"] = log_in_view_controller
        self._controller["log_in"].log_in_finished.connect(self.initialise_data)

        self.change_view("log_in")

    @QtCore.pyqtSlot(str)
    def initialise_data(self, user_id):

        self._model = Model(FetchEngine(FhirApiFetcherProtocol()), str(user_id))
        for patient in self._model._list_of_patients:
            print(patient.name)
            print(patient.id)
            print(patient.observations['Cholesterol'].value)

        list_of_patients_view_controller = MyListOfPatientsViewController()
        self._views["list_of_patients"] = MyListOfPatients(self._model, list_of_patients_view_controller)

        list_of_monitored_patients_view_controller = MyListOfMonitoredPatientsViewController()
        self._views["list_of_monitored_patients"] = MyListOfMonitoredPatients(self._model,
                                                                              list_of_monitored_patients_view_controller)

        self._controller["list_of_patients"] = list_of_patients_view_controller
        self._controller["list_of_patients"].list_of_patients_finished.connect(self.change_view)

        self._controller["list_of_monitored_patients"] = list_of_monitored_patients_view_controller
        self._controller["list_of_monitored_patients"].list_of_monitored_patients_finished.connect(self.change_view)

        self.change_view("list_of_patients")

    @QtCore.pyqtSlot(str)
    def change_view(self, view_name):
        view = self._views.get(view_name)
        if view is not None:
            view.show()


if __name__ =='__main__':
    app = Application(sys.argv)
    sys.exit(app.exec())
