from DataModel.Patient import Patient


class Monitor:

    def __init__(self, subject_of_monitor: Patient, frequency_of_update):
        assert type(subject_of_monitor) is Patient, "Subject of monitor must be a patient but it is " + \
                                                    str(type(subject_of_monitor))

        self.subject_of_monitor = subject_of_monitor
        self.frequency_of_update = frequency_of_update
