import urllib.request
import json
from abc import ABC, abstractmethod
from DataModel.Patient import Patient
from DataModel.Observation import Observation


class MedicalApiFetcherProtocol(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def fetch_patient(self, patient_id: str) -> Patient:
        assert type(patient_id) is str, "patient_id should have type string but is " + str(type(patient_id))

    @abstractmethod
    def fetch_patient_of_practitioner(self, practitioner_id: str) -> [Patient]:
        assert type(practitioner_id) is str, "practitioner_id should have type string but is " + \
                                             str(type(practitioner_id))

    @abstractmethod
    def fetch_patient_measurements(self, patient_id: str) -> {Observation}:
        assert type(patient_id) is str, "patient_id should have type string but is " + str(type(patient_id))

    def _fetch(self, url):

        assert type(url) is str, "url should be a string but is " + str(type(url))

        request = urllib.request.Request(url)

        try:
            requested_data_json = urllib.request.urlopen(request).read()
        except Exception as e:
            print("Failed to fetch data with URL: " + url)
            raise

        requested_data = json.loads(requested_data_json)

        return requested_data
