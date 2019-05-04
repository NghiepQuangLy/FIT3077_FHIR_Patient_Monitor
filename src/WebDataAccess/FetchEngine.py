from WebDataAccess.MedicalApiFetcherProtocol import MedicalApiFetcherProtocol
from DataModel.Patient import Patient
from DataModel.Observation import Observation


class FetchEngine:

    def __init__(self, fetch_protocol: MedicalApiFetcherProtocol):
        assert issubclass(type(fetch_protocol), MedicalApiFetcherProtocol), "fetch protocol does not conform to " \
                                                                            "MedicalApiFetcherProtocol but it is of " \
                                                                            "type " + str(type(fetch_protocol))
        self.__fetch_protocol = fetch_protocol

    def fetch_patient(self, patient_id: str) -> Patient:
        assert type(patient_id) is str, "Patient id should be a string but it is of type " + str(type(patient_id))
        return self.__fetch_protocol.fetch_patient(patient_id)

    def fetch_patient_of_practitioner(self, practitioner_id: str) -> [Patient]:
        assert type(practitioner_id) is str, "Practitioner id should be a string but it is of type" + \
                                             str(type(practitioner_id))
        return self.__fetch_protocol.fetch_patient_of_practitioner(practitioner_id)

    def fetch_patient_measurements(self, patient_id: str) -> {Observation}:
        assert type(patient_id) is str, "Patient id should be a string but it is of type " + str(type(patient_id))
        return self.__fetch_protocol.fetch_patient_measurements(patient_id)
