import urllib.request
import json
from abc import ABC, abstractmethod
from Patient import Patient
from Practitioner import Practitioner

FHIR_URL = "http://hapi-fhir.erc.monash.edu:8080/baseDstu3/"
PATIENT_EXTENSION = "Patient/"
PRACTITIONER_EXTENSION = "Practitioner/"

class FhirApiFetcherProtocol(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def fetchPatient(self, patient_id: int) -> Patient:
        pass

    @abstractmethod
    def fetchPractitioner(self, practitioner_id: int) -> Practitioner:
        pass

    @abstractmethod
    def fetchPatientOfPractitioner(self, practitioner_id: int, patient_id: int) -> [Patient]:
        pass

class Fetch():

    def _fetch(self, url):

        if type(url) is not str:
            raise TypeError("url should be a string but is " + str(type(url)))

        request = urllib.request.Request(url)

        try:
            requested_data_json = urllib.request.urlopen(request).read()
        except Exception as e:
            print("Failed to fetch data with URL: " + url)
            raise

        requested_data = json.loads(requested_data_json)

        return requested_data

class FhirApiFetcher(FhirApiFetcherProtocol, Fetch):

    def fetchPatient(self, patient_id: int) -> Patient:

        if type(patient_id) is not int:
            raise TypeError("patient_id should have type integer but is " + str(type(patient_id)))

        patient_url = FHIR_URL + PATIENT_EXTENSION + str(patient_id)

        patient_data = self._fetch(patient_url)

        return Patient()

    def fetchPractitioner(self, practitioner_id: int) -> Practitioner:

        if type(practitioner_id) is not int:
            raise TypeError("practitioner_id should have type integer but is " + str(type(practitioner_id)))

        super.fetchPractitioner(practitioner_id)

        practitioner_url = FHIR_URL + PRACTITIONER_EXTENSION + str(practitioner_id)

        practitioner_data = self._fetch(practitioner_url)

        return Practitioner()

thing = FhirApiFetcher()
print(thing.fetchPractitioner('sd').name)
