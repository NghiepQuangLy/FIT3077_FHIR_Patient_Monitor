from DataModel.MedicalApiFetcherProtocol import MedicalApiFetcherProtocol
from DataModel.Patient import Patient
from DataModel.Practitioner import Practitioner
from DataModel.Observation import Observation
from DataModel.Cholesterol import Cholesterol


class FhirApiFetcher(MedicalApiFetcherProtocol):

    FHIR_URL = "http://hapi-fhir.erc.monash.edu:8080/baseDstu3/"
    PATIENT_EXTENSION = "Patient"
    PRACTITIONER_EXTENSION = "Practitioner"
    ENCOUNTER_EXTENSION = "Encounter"
    OBSERVATION_EXTENSION = "Observation"

    def fetch_patient(self, patient_id: str) -> Patient:

        super().fetch_patient(patient_id)

        try:
            int(patient_id)
        except ValueError as e:
            err_msg = "FHIR uses only integers for their patient id but input is ", patient_id
            e.args = err_msg
            raise

        patient_url = self.FHIR_URL + self.PATIENT_EXTENSION + "/" + str(patient_id)

        patient_data = self._fetch(patient_url)

        patient = Patient(patient_data['id'],
                          patient_data['name'][0]['given'][0] + " " + patient_data['name'][0]['family'])

        return patient

    def fetch_practitioner(self, practitioner_id: str) -> Practitioner:

        super().fetch_practitioner(practitioner_id)

        try:
            int(practitioner_id)
        except ValueError as e:
            err_msg = "FHIR uses only integers for their practitioner id but input id is ", practitioner_id
            e.args = err_msg
            raise

        practitioner_url = self.FHIR_URL + self.PRACTITIONER_EXTENSION + "/" + str(practitioner_id)

        practitioner_data = self._fetch(practitioner_url)

        practitioner = Practitioner(practitioner_data['id'],
                                    practitioner_data['name'][0]['given'][0] + " " +
                                    practitioner_data['name'][0]['family'])

        return practitioner

    def fetch_patient_of_practitioner(self, practitioner_id: str) -> [Patient]:

        super().fetch_patient_of_practitioner(practitioner_id)

        try:
            int(practitioner_id)
        except ValueError as e:
            err_msg = "FHIR uses only integers for their practitioner id but input id is ", practitioner_id
            e.args = err_msg
            raise

        practitioner_encounter_list_url = self.FHIR_URL + self.ENCOUNTER_EXTENSION + "?practitioner=" + \
                                        str(practitioner_id)

        practitioner_encounter_list_data = self._fetch(practitioner_encounter_list_url)

        patient_ids = set()
        patient_list = []

        for encounter in practitioner_encounter_list_data['entry']:
            patient_id = encounter['resource']['subject']['reference'].replace("Patient/", "")
            patient_ids.add(patient_id)

        for patient_id in patient_ids:
            patient_list.append(self.fetch_patient(patient_id))

        return patient_list

    def fetch_patient_measurements(self, patient_id: str) -> {Observation}:

        super().fetch_patient_measurements(patient_id)

        try:
            int(patient_id)
        except ValueError as e:
            err_msg = "FHIR uses only integers for their patient id but input id is ", patient_id
            e.args = err_msg
            raise

        patient_measurements_url = self.FHIR_URL + self.OBSERVATION_EXTENSION + "?subject=" + str(patient_id)

        patient_measurements_data = self._fetch(patient_measurements_url)

        patient_measurements_all = {}
        for measurement in patient_measurements_data['entry']:
            try:
                patient_measurements_all[measurement['resource']['code']['text']] = measurement['resource']['valueQuantity']
            except:
                patient_measurements_all[measurement['resource']['code']['text']] = \
                    measurement['resource']['valueCodeableConcept']['text']

        cholesterol = Cholesterol(patient_measurements_all['Total Cholesterol']['value'],
                                  patient_measurements_all['Total Cholesterol']['unit'])

        patient_measurements_relevant = {cholesterol.name: cholesterol}

        return patient_measurements_relevant

thing = FhirApiFetcher()
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
