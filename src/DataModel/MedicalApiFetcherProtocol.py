from abc import ABC, abstractmethod
from DataModel.Practitioner import Practitioner
from DataModel.Patient import Patient


class MedicalApiFetcherProtocol(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def fetch_patient(self, patient_id: str) -> Patient:

        if type(patient_id) is not str:
            raise TypeError("patient_id should have type string but is " + str(type(patient_id)))

    @abstractmethod
    def fetch_practitioner(self, practitioner_id: str) -> Practitioner:

        if type(practitioner_id) is not str:
            raise TypeError("practitioner_id should have type string but is " + str(type(practitioner_id)))


    @abstractmethod
    def fetch_patient_of_practitioner(self, practitioner_id: str, patient_id: str) -> [Patient]:

        if type(practitioner_id) is not int:
            raise TypeError("practitioner_id should have type string but is " + str(type(practitioner_id)))

        if type(patient_id) is not int:
            raise TypeError("patient_id should have type string but is " + str(type(patient_id)))
