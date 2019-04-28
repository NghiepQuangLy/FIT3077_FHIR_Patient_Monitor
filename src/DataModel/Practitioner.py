from DataModel.Patient import Patient


class Practitioner:

    def __init__(self, id: str, name: str, list_of_patients: [Patient] = []):

        if type(id) is not str:
            raise TypeError("id should be an string but is " + str(type(id)))

        if type(name) is not str:
            raise TypeError("name should be a string but is " + str(type(name)))

        for patient in list_of_patients:
            if patient is not Patient:
                raise TypeError("A patient in a list of patients needs to be of class Patient but is " +
                                str(type(patient)))

        self.id = id
        self.name = name
        self.list_of_patients = list_of_patients