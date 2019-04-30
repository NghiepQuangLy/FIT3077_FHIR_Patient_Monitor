from DataModel.FhirApiFetcherProtocol import FhirApiFetcherProtocol
from DataModel.MedicalApiFetcherProtocol import MedicalApiFetcherProtocol


class FetchEngine:

    def __init__(self, fetch_protocol: MedicalApiFetcherProtocol):
        assert issubclass(type(fetch_protocol), MedicalApiFetcherProtocol), "fetch protocol does not conform to " \
                                                                            "MedicalApiFetcherProtocol but it is of " \
                                                                            "type " + str(type(fetch_protocol))
        self.__fetch_protocol = FhirApiFetcherProtocol()

    def fetch_patient(self, patient_id: str):
        self.__fetch_protocol.fetch_patient(patient_id)

    def fetch_practitioner(self, patient_id: str):
        self.__fetch_protocol.fetch_practitioner(patient_id)

    def fetch_patient_of_practitioner(self, practitioner_id: str):
        self.__fetch_protocol.fetch_patient_of_practitioner(practitioner_id)

    def fetch_patient_measurements(self, patient_id: str):
        self.__fetch_protocol.fetch_patient_measurements(patient_id)


thing = FhirApiFetcherProtocol()
a = thing.fetch_practitioner('275')
print(a.name)
print(a.id)
b = thing.fetch_patient('1')
print(b.name)
print(b.id)
new = thing.fetch_patient_of_practitioner('275')
for patient in new:
    print(patient.id)
    print(patient.name)
athing = thing.fetch_patient_measurements('1')

for thing in athing:
    print(athing[thing].get_description())