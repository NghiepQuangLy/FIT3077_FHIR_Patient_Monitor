from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from DataModel.Model import Model
from View.PyQt5GeneratedUis.ListOfPatientsView import UiListOfPatients
from View.CustomPatientListItemWidget import CustomPatientListItemWidget
from Controller import MyListOfPatientsViewController


class MyListOfPatients(QtWidgets.QWidget):

    def __init__(self, model: Model, controller: MyListOfPatientsViewController):
        super().__init__()

        self._model = model
        self._controller = controller
        self._ui = UiListOfPatients()
        self._ui.setupUi(self)
        self.load_list(self._model._list_of_unmonitored_patients['cholesterol'])
        self._ui.showMonitoredPatientButton.clicked.connect(self.show_monitored_patients)
        self._controller.list_of_patients_finished.connect(self.hide)

    @pyqtSlot()
    def show_monitored_patients(self):
        self._controller.show_monitored_patients()

    def load_list(self, patient_list):

        default_list_item = QtWidgets.QListWidgetItem()

        for patient in patient_list:

            patient_list_item = CustomPatientListItemWidget(patient.name, "Monitor", self.monitor_patient, patient.id)

            default_list_item.setSizeHint(patient_list_item.sizeHint())

            self._ui.allPatientListWidget.addItem(default_list_item)
            self._ui.allPatientListWidget.setItemWidget(default_list_item, patient_list_item)

    def update(self, subject_state):
        self._ui.allPatientListWidget.clear()
        self.load_list(self._model._list_of_unmonitored_patients['cholesterol'])
        print("hello")

    @pyqtSlot()
    def monitor_patient(self):
        patient_id_selected = self.sender().objectName()
        self._model.remove_unmonitored_patient(patient_id_selected, 'cholesterol')
        monitored_patient = self._model.get_patient(patient_id_selected)
        self._model.add_monitored_patient(monitored_patient, 'cholesterol')
        print(patient_id_selected)
