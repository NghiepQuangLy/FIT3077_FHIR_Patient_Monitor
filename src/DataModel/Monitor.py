from DataModel.Patient import Patient


class Monitor:

    def __init__(self, name: str, subject_of_monitor: Patient):
        assert type(name) is str, "Monitor's name must be a string but it is " + str(type(name))
        assert type(subject_of_monitor) is Patient, "Subject of monitor must be a patient but it is " + \
                                                    str(type(subject_of_monitor))

        self.name = name
        self.subject_of_monitor = subject_of_monitor
