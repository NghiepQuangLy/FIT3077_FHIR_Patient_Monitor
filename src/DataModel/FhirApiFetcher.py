from DataModel.MedicalApiFetcherProtocol import MedicalApiFetcherProtocol
from DataModel.Fetch import Fetch
from DataModel.Patient import Patient
from DataModel.Practitioner import Practitioner


class FhirApiFetcher(MedicalApiFetcherProtocol, Fetch):

    FHIR_URL = "http://hapi-fhir.erc.monash.edu:8080/baseDstu3/"
    PATIENT_EXTENSION = "Patient/"
    PRACTITIONER_EXTENSION = "Practitioner/"

    def fetch_patient(self, patient_id: str) -> Patient:

        super().fetch_patient(patient_id)

        try:
            int(patient_id)
        except ValueError as e:
            err_msg = "FHIR uses only integers for their patient id but input is ", patient_id
            e.args = (err_msg)
            raise

        patient_url = self.FHIR_URL + self.PATIENT_EXTENSION + str(patient_id)

        patient_data = self._fetch(patient_url)

        return Patient()

    def fetch_practitioner(self, practitioner_id: str) -> Practitioner:

        super().fetch_practitioner(practitioner_id)

        try:
            int(practitioner_id)
        except ValueError as e:
            err_msg = "FHIR uses only integers for their practitioner id but input id is ", practitioner_id
            e.args = (err_msg)
            raise

        practitioner_url = self.FHIR_URL + self.PRACTITIONER_EXTENSION + str(practitioner_id)

        practitioner_data = self._fetch(practitioner_url)
        print(practitioner_data)
        practitioner = Practitioner(practitioner_data['id'],
                                    practitioner_data['name'][0]['given'][0] + " " +
                                    practitioner_data['name'][0]['family'])

        return practitioner

    def fetch_patient_of_practitioner(self, practitioner_id: str, patient_id: str) -> [Patient]:

        super().fetch_patient_of_practitioner(practitioner_id, patient_id)

        return [Patient()]

thing = FhirApiFetcher()
a = thing.fetch_practitioner('275')
print(a.name)
print(a.id)
