from abc import ABC, abstractmethod
from DataModel.Patient import Patient


class ModelProtocol(ABC):

    user_id: int
    _list_of_patients = []
    _list_of_unmonitored_patients = {"cholesterol": []}
    _list_of_monitors = {"cholesterol": []}

    def __init__(self):
        super().__init__()

    @abstractmethod
    def add_patient(self, patient: Patient):
        assert type(patient) is Patient, "Patient id should be a string but it is of type " + str(type(patient_id))
        pass

    @abstractmethod
    def get_patient(self, patient_id: str):
        assert type(patient_id) is str, "Patient id should be a string but it is of type " + str(type(patient_id))
        pass

    @abstractmethod
    def add_unmonitored_patient(self, patient: Patient, unmonitored_value: str):
        assert type(patient) is Patient, "Patient should be an instance of the Patient class but it is of type " + \
                                         str(type(patient))
        assert type(unmonitored_value) is str, "Unmonitored value should be of type string but it is of type " + \
                                               str(type(unmonitored_value))
        pass

    @abstractmethod
    def add_monitored_patient(self, patient: Patient, value_for_monitor: str):
        assert type(patient) is Patient, "Patient should be an instance of the Patient class but it is of type " + \
                                         str(type(patient))
        assert type(value_for_monitor) is str, "Unmonitored value should be of type string but it is of type " + \
                                               str(type(value_for_monitor))
        pass

    @abstractmethod
    def remove_unmonitored_patient(self, patient_id: str, unmonitored_value: str):
        assert type(patient_id) is str, "Patient id should be a string but it is of type " + str(type(patient_id))
        pass

    @abstractmethod
    def remove_monitored_patient(self, patient_id: str, value_for_monitor: str):
        assert type(patient_id) is str, "Patient id should be a string but it is of type " + str(type(patient_id))
        pass
