from WebDataAccess.MedicalApiFetcherProtocol import MedicalApiFetcherProtocol
from DataModel.Patient import Patient
from DataModel.Observation import Observation
from DataModel.Cholesterol import Cholesterol


class FhirApiFetcherProtocol(MedicalApiFetcherProtocol):

    _FHIR_URL = "http://hapi-fhir.erc.monash.edu:8080/baseDstu3/"
    _PATIENT_EXTENSION = "Patient"
    _PRACTITIONER_EXTENSION = "Practitioner"
    _ENCOUNTER_EXTENSION = "Encounter"
    _OBSERVATION_EXTENSION = "Observation"
    _CHOLESTEROL_CODE = "2093-3"

    def fetch_patient(self, patient_id: str) -> Patient:

        super().fetch_patient(patient_id)

        try:
            int(patient_id)
        except ValueError as e:
            err_msg = "FHIR uses only integers for their patient id but input is ", patient_id
            e.args = err_msg
            raise

        patient_url = self._FHIR_URL + self._PATIENT_EXTENSION + "/" + str(patient_id)

        patient_data = self._fetch(patient_url)
        patient_measurements = self.fetch_patient_measurements(str(patient_id))
        patient = Patient(patient_data['id'],
                          patient_data['name'][0]['given'][0] + " " + patient_data['name'][0]['family'],
                          patient_measurements)

        return patient

    def fetch_patient_of_practitioner(self, practitioner_id: str) -> [Patient]:

        super().fetch_patient_of_practitioner(practitioner_id)

        try:
            int(practitioner_id)
        except ValueError as e:
            err_msg = "FHIR uses only integers for their practitioner id but input id is ", practitioner_id
            e.args = err_msg
            raise

        practitioner_encounter_list_url = self._FHIR_URL + self._ENCOUNTER_EXTENSION + "?practitioner=" + \
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

        cholesterol = self.__fetch_patient_cholesterol(patient_id)

        patient_measurements_all = {}

        if cholesterol is not None:
            patient_measurements_all["Cholesterol"] = cholesterol

        return patient_measurements_all

    def __fetch_patient_cholesterol(self, patient_id: str) -> Cholesterol:

        patient_cholesterol_url = self._FHIR_URL + self._OBSERVATION_EXTENSION + "?code=" + self._CHOLESTEROL_CODE + \
                                   "&subject=" + str(patient_id)

        patient_cholesterol_data = self._fetch(patient_cholesterol_url)

        try:
            value = patient_cholesterol_data['entry'][0]['resource']['valueQuantity']['value']
            unit = patient_cholesterol_data['entry'][0]['resource']['valueQuantity']['unit']
        except:
            return None

        return Cholesterol(value, unit)
