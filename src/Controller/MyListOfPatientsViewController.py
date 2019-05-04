from PyQt5 import QtCore
from DataModel.ModelProtocol import ModelProtocol

class MyListOfPatientsViewController(QtCore.QObject):

    list_of_patients_finished = QtCore.pyqtSignal(str)

    def __init__(self, model: ModelProtocol):
        super().__init__()

        # assert issubclass(model, ModelProtocol), "model should conform to the Model Protocol"
        self._model = model

    def show_monitored_patients(self):
        self.list_of_patients_finished.emit("list_of_monitored_patients")

    def monitor_patient(self, patient_id: str, value_for_monitor: str):
        assert type(patient_id) is str, "Patient id should be a string but it is of type " + str(type(patient_id))
        assert type(value_for_monitor) is str, "Value for monitor should be a string but it is of type " + \
                                               str(type(value_for_monitor))

        self._model.remove_unmonitored_patient(patient_id, value_for_monitor)
        monitored_patient = self._model.get_patient(patient_id)
        self._model.add_monitored_patient(monitored_patient, value_for_monitor)
        print(patient_id)
