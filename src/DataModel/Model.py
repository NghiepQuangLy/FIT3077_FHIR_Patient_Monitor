from WebDataAccess.FetchEngine import FetchEngine
from DataModel.ModelProtocol import ModelProtocol
from DataModel.Patient import Patient
from Observer.Subject import Subject
import threading


class Model(ModelProtocol, Subject):

    def __init__(self, fetch_engine: FetchEngine, user_id: int, update_frequency: int = 5):

        assert type(fetch_engine) is FetchEngine, "fetch engine needs to be of type FetchEngine but it is " + \
                                                 str(type(fetch_engine))
        assert type(user_id) is str, "user id should be of type string but it is of type " + str(type(user_id))
        assert type(update_frequency) is int, "update frequency should be of type int but it is of type " + \
                                              str(type(update_frequency))

        self.__fetch_engine = fetch_engine
        self.__user_id = user_id
        self.__update_frequency = update_frequency

        list_of_patients = self.__fetch_engine.fetch_patient_of_practitioner(user_id)

        for patient in list_of_patients:
            self.add_patient(patient)
            self.add_unmonitored_patient(patient, "cholesterol")

        #self._update_monitored_patient_data()

    def add_patient(self, patient: Patient):

        super().add_patient(patient)

        self._list_of_patients.append(patient)

        self.set_state()
        self._notify()

    def add_unmonitored_patient(self, patient: Patient, unmonitored_value: str):

        super().add_unmonitored_patient(patient, unmonitored_value)

        try:
            self._list_of_unmonitored_patients[unmonitored_value].append(patient)
        except:
            self._list_of_unmonitored_patients[unmonitored_value] = []
            self._list_of_unmonitored_patients[unmonitored_value].append(patient)

        self.set_state()
        self._notify()

    def add_monitored_patient(self, patient: Patient, value_for_monitor: str):

        super().add_monitored_patient(patient, value_for_monitor)

        try:
            self._list_of_monitors[value_for_monitor].append(patient)
        except:
            self._list_of_monitors[value_for_monitor] = []
            self._list_of_monitors[value_for_monitor].append(patient)

        self.set_state()
        self._notify()

    def remove_unmonitored_patient(self, patient_id: str, unmonitored_value: str):

        super().remove_unmonitored_patient(patient_id, unmonitored_value)

        try:
            for index in range(len(self._list_of_unmonitored_patients[unmonitored_value])):
                current_patient = self._list_of_unmonitored_patients[unmonitored_value][index]
                if patient_id == current_patient.id:
                    break
            self._list_of_unmonitored_patients[unmonitored_value].pop(index)
        except:
            pass

        self.set_state()
        self._notify()

    def remove_monitored_patient(self, patient_id: str, value_for_monitor: str):

        super().remove_monitored_patient(patient_id, value_for_monitor)

        try:
            for index in range(len(self._list_of_monitors[value_for_monitor])):
                current_patient = self._list_of_monitors[value_for_monitor][index]
                if patient_id == current_patient.id:
                    break
            self._list_of_monitors[value_for_monitor].pop(index)
        except:
            pass

        self.set_state()
        self._notify()

    def get_patient(self, patient_id: str):

        super().get_patient(patient_id)

        for patient in self._list_of_patients:
            if patient_id == patient.id:
                return patient

    def set_state(self):
        self._subject_state = {"list_of_patients": self._list_of_patients,
                               "list_of_monitors": self._list_of_monitors}

    def _update_monitored_patient_data(self):

        unique_patient_id_set = set()
        #
        for type_of_monitors in self._list_of_monitors:
            for patient in self._list_of_monitors[type_of_monitors]:
                unique_patient_id_set.add(patient.id)
        #
        for patient_id in unique_patient_id_set:
            patient = self.get_patient(patient_id)
            patient.set_medical_data(self.__fetch_engine.fetch_patient_measurements(patient_id))

        if len(unique_patient_id_set) != 0:
            print(len(unique_patient_id_set))
            self.set_state()
            self._notify()

        print("hello")

        threading.Timer(self.__update_frequency, self._update_monitored_patient_data).start()
