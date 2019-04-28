from abc import ABC, abstractmethod
from DataModel.Practitioner import Practitioner
from DataModel.Patient import Patient
from DataModel.Measurements import Measurements

class MedicalApiFetcherProtocol(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def fetch_patient(self, patient_id: str) -> Patient:
        assert type(patient_id) is str, "patient_id should have type string but is " + str(type(patient_id))

    @abstractmethod
    def fetch_practitioner(self, practitioner_id: str) -> Practitioner:
        assert type(practitioner_id) is str, "practitioner_id should have type string but is " + \
                                             str(type(practitioner_id))

    @abstractmethod
    def fetch_patient_of_practitioner(self, practitioner_id: str) -> [Patient]:
        assert type(practitioner_id) is str, "practitioner_id should have type string but is " + \
                                             str(type(practitioner_id))

    #@abstractmethod
    #def fetch_patient_measurements(self, patient_id: str) -> Measurements:
     #   assert type(patient_id) is str, "patient_id should have type string but is " + str(type(patient_id))
