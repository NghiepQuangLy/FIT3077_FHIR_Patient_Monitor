from PyQt5.QtCore import QObject, pyqtSignal
from WebDataAccess.FetchEngine import FetchEngine
from DataModel.ModelProtocol import ModelProtocol
from DataModel.Patient import Patient


class Model(QObject, ModelProtocol):

    def __init__(self, fetch_engine: FetchEngine):
        assert type(fetch_engine) is FetchEngine, "fetch engine needs to be of type FetchEngine but it is " + \
                                                 str(type(fetch_engine))

    def add_patient(self, patient: Patient):
        self.list_of_patients.append(Patient)

    def add_monitored_patient(self, patient: Patient, value_for_monitor: str):
        try:
            self.list_of_monitors[value_for_monitor].append(patient)
        except:
            self.list_of_monitors[value_for_monitor] = []
            self.list_of_monitors[value_for_monitor].append(patient)

    def remove_monitored_patient(self, patient: Patient, value_for_monitor: str):
        try:
            self.list_of_monitors[value_for_monitor].remove(patient)
        except:
            pass
