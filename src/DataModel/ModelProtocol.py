from abc import ABC, abstractmethod
from DataModel.Patient import Patient


class ModelProtocol(ABC):

    user_id: int
    _list_of_patients = []
    _list_of_monitors = {"cholesterol": []}

    def __init__(self):
        super().__init__()

    @abstractmethod
    def add_monitored_patient(self, patient: Patient, value_for_monitor: str):
        pass

    @abstractmethod
    def remove_monitored_patient(self, patient: Patient, value_for_monitor: str):
        pass

    @abstractmethod
    def add_patient(self, patient_id: str):
        pass
