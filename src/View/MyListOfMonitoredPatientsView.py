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

    def load_list(self, monitored_patient_list):

        default_list_item = QtWidgets.QListWidgetItem()

        for patient in monitored_patient_list:
            patient_list_item = CustomPatientListItemWidget(patient.name, "Unmonitor",
                                                            self.unmonitor_patient, patient.id)

            default_list_item.setSizeHint(patient_list_item.sizeHint())

            self._ui.monitoredPatientListWidget.addItem(default_list_item)
            self._ui.monitoredPatientListWidget.setItemWidget(default_list_item, patient_list_item)

    def update(self, subject_state):
        self._ui.monitoredPatientListWidget.clear()
        self.load_list(self._model._list_of_monitors['cholesterol'])
        print("hello monitored")

    @pyqtSlot()
    def unmonitor_patient(self):
        patient_id_selected = self.sender().objectName()
        self._model.remove_monitored_patient(patient_id_selected, 'cholesterol')
        unmonitored_patient = self._model.get_patient(patient_id_selected)
        self._model.add_unmonitored_patient(unmonitored_patient, 'cholesterol')
        print("unmonitor")