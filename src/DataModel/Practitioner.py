from DataModel.Patient import Patient
from DataModel.Monitor import Monitor


class Practitioner:

    def __init__(self, id: str, name: str, list_of_patients: [Patient] = [],
                 list_of_monitors: [Monitor] = []):

        assert type(id) is str, "practitioner id should be a string but is " + str(type(id))
        assert type(name) is str, "practitioner name should be a string but is " + str(type(name))

        for patient in list_of_patients:
            assert type(patient) is Patient, "A patient in a list of patients should be an instance of Patient class" \
                                             "but is " + str(type(patient))

        for monitor in list_of_monitors:
            assert type(monitor) is Monitor, "A monitor in a list of monitors should be an instance of " \
                                             "Monitor class but is " + str(type(monitor))

        self.id = id
        self.name = name
        self.list_of_patients = list_of_patients
        self.list_of_monitors = list_of_monitors

    def set_patients(self, list_of_patients: [Patient]):

        for patient in list_of_patients:
            assert type(patient) is Patient, "A patient in a list of patients should be an instance of Patient class" \
                                             "but is " + str(type(patient))

        self.list_of_patients = list_of_patients

    def add_monitor(self, monitor: Monitor):
        assert type(monitor) is Monitor, "A monitor should be an instance of Monitor class but is " + str(type(monitor))
        self.list_of_monitors.append(monitor)
