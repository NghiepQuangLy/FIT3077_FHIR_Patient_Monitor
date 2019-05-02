from abc import ABC, abstractmethod
from PyQt5.QtCore import pyqtSignal
from DataModel.Patient import Patient
from DataModel.Practitioner import Practitioner
from DataModel.Monitor import Monitor
from DataModel.Observation import Observation


class ModelProtocol(ABC):

    list_of_patients_changed = pyqtSignal(int)
    list_of_monitored_patients_changed = pyqtSignal()
    monitored_patient_info_change = pyqtSignal()

    list_of_patients = []
    list_of_monitors = {"cholesterol": []}

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
