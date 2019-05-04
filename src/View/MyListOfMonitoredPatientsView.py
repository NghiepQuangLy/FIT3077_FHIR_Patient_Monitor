from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from DataModel.Model import Model
from View.PyQt5GeneratedUis.ListOfMonitoredPatientsView import UiListOfMonitoredPatients
from View.CustomPatientListItemWidget import CustomPatientListItemWidget
from Controller import MyListOfMonitoredPatientsViewController


class MyListOfMonitoredPatients(QtWidgets.QWidget):

    def __init__(self, model: Model, controller: MyListOfMonitoredPatientsViewController):
        super().__init__()

        self._model = model
        self._controller = controller
        self._ui = UiListOfMonitoredPatients()
        self._ui.setupUi(self)
        self.load_list(self._model._list_of_monitors["cholesterol"])
        self._ui.showAllPatientButton.clicked.connect(self.show_all_patients)
        self._controller.list_of_monitored_patients_finished.connect(self.hide)

    @pyqtSlot()
    def show_all_patients(self):
        self._controller.show_all_patients()

    @pyqtSlot()
    def unmonitor_patient(self):
        patient_id_selected = self.sender().objectName()
        self._controller.unmonitor_patient(patient_id_selected,
                                           str(self._ui.monitoredPatientListTypeSelector.currentText()).lower())

    def load_list(self, monitored_patient_list):

        current_list_type = str(self._ui.monitoredPatientListTypeSelector.currentText())

        for patient in monitored_patient_list:

            try:
                patient_measurement = patient.observations[current_list_type].get_description()
            except:
                patient_measurement = ""

            default_list_item = QtWidgets.QListWidgetItem()

            patient_list_item = CustomPatientListItemWidget(patient.name, "Unmonitor", self.unmonitor_patient,
                                                            patient.id, patient_measurement)

            default_list_item.setSizeHint(patient_list_item.sizeHint())

            self._ui.monitoredPatientListWidget.addItem(default_list_item)
            self._ui.monitoredPatientListWidget.setItemWidget(default_list_item, patient_list_item)

    def update(self, subject_state):
        self._ui.monitoredPatientListWidget.clear()
        self.load_list(self._model._list_of_monitors['cholesterol'])
        print("hello monitored")
