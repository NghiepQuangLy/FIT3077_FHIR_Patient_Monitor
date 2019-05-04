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

    @pyqtSlot()
    def monitor_patient(self):
        patient_id_selected = self.sender().objectName()
        self._controller.monitor_patient(patient_id_selected,
                                         str(self._ui.allPatientListSortSelector.currentText()).lower())

    def load_list(self, patient_list):

        current_list_type = str(self._ui.allPatientListSortSelector.currentText())

        for patient in patient_list:

            try:
                patient_measurement = patient.observations[current_list_type].get_description()
            except:
                patient_measurement = ""

            default_list_item = QtWidgets.QListWidgetItem()

            patient_list_item = CustomPatientListItemWidget(patient.name, "Monitor", self.monitor_patient, patient.id,
                                                            patient_measurement)

            default_list_item.setSizeHint(patient_list_item.sizeHint())

            self._ui.allPatientListWidget.addItem(default_list_item)
            self._ui.allPatientListWidget.setItemWidget(default_list_item, patient_list_item)

    def update(self, subject_state):
        self._ui.allPatientListWidget.clear()
        self.load_list(self._model._list_of_unmonitored_patients['cholesterol'])
        print("hello")
