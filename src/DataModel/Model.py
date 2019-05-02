from WebDataAccess.FetchEngine import FetchEngine
from DataModel.ModelProtocol import ModelProtocol
from DataModel.Patient import Patient
from Observer.Subject import Subject


class Model(ModelProtocol, Subject):

    def __init__(self, fetch_engine: FetchEngine, user_id: int):
        assert type(fetch_engine) is FetchEngine, "fetch engine needs to be of type FetchEngine but it is " + \
                                                 str(type(fetch_engine))
        self.__fetch_engine = fetch_engine
        self.__user_id = user_id

        list_of_patients = self.__fetch_engine.fetch_patient_of_practitioner(user_id)

        for patient in list_of_patients:
            self.add_patient(patient)

    def add_patient(self, patient: Patient):
        self.list_of_patients.append(Patient)
        self._notify(self.get_state())

    def add_monitored_patient(self, patient: Patient, value_for_monitor: str):
        try:
            self.list_of_monitors[value_for_monitor].append(patient)
        except:
            self.list_of_monitors[value_for_monitor] = []
            self.list_of_monitors[value_for_monitor].append(patient)
        self._notify(self.get_state())

    def remove_monitored_patient(self, patient: Patient, value_for_monitor: str):
        try:
            self.list_of_monitors[value_for_monitor].remove(patient)
        except:
            pass
        self._notify(self.get_state())

    def get_state(self):
        return {
            "list_of_patients": self._list_of_patients,
            "list_of_monitors": self._list_of_monitors
        }
