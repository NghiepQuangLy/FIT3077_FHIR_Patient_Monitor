from WebDataAccess.FhirApiFetcherProtocol import FhirApiFetcherProtocol
from WebDataAccess.MedicalApiFetcherProtocol import MedicalApiFetcherProtocol


class FetchEngine:

    def __init__(self, fetch_protocol: MedicalApiFetcherProtocol):
        assert issubclass(type(fetch_protocol), MedicalApiFetcherProtocol), "fetch protocol does not conform to " \
                                                                            "MedicalApiFetcherProtocol but it is of " \
                                                                            "type " + str(type(fetch_protocol))
        self.__fetch_protocol = fetch_protocol

    def fetch_patient(self, patient_id: str):
        return self.__fetch_protocol.fetch_patient(patient_id)

    def fetch_practitioner(self, patient_id: str):
        return self.__fetch_protocol.fetch_practitioner(patient_id)

    def fetch_patient_of_practitioner(self, practitioner_id: str):
        return self.__fetch_protocol.fetch_patient_of_practitioner(practitioner_id)

    def fetch_patient_measurements(self, patient_id: str):
        return self.__fetch_protocol.fetch_patient_measurements(patient_id)
