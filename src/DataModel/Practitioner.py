from DataModel.Patient import Patient


class Practitioner:

    def __init__(self, id: str, name: str, list_of_patients: [Patient] = []):

        assert type(id) is str, "practitioner id should be a string but is " + str(type(id))
        assert type(name) is str, "practitioner name should be a string but is " + str(type(name))

        for patient in list_of_patients:

            assert type(patient) is Patient, "A patient in a list of patients should be an instance of Patient class" \
                                             "but is " + str(type(patient))

        self.id = id
        self.name = name
        self.list_of_patients = list_of_patients

    def set_patients(self, list_of_patients: [Patient]):

        for patient in list_of_patients:
            assert type(patient) is Patient, "A patient in a list of patients should be an instance of Patient class" \
                                             "but is " + str(type(patient))

