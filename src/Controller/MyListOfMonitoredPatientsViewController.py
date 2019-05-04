from PyQt5 import QtCore


class MyListOfMonitoredPatientsViewController(QtCore.QObject):

    list_of_monitored_patients_finished = QtCore.pyqtSignal(str)

    def __init__(self, model):
        super().__init__()

        # assert issubclass(model, ModelProtocol), "model should conform to the Model Protocol"
        self._model = model

    def show_all_patients(self):
        self.list_of_monitored_patients_finished.emit("list_of_patients")

    def unmonitor_patient(self, patient_id: str, unmonitored_value: str):
        assert type(patient_id) is str, "Patient id should be a string but it is of type " + str(type(patient_id))
        assert type(unmonitored_value) is str, "Unmonitored value should be a string but it is of type " + \
                                               str(type(unmonitored_value))

        self._model.remove_monitored_patient(patient_id, unmonitored_value)
        unmonitored_patient = self._model.get_patient(patient_id)
        self._model.add_unmonitored_patient(unmonitored_patient, unmonitored_value)
