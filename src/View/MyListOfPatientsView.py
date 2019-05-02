from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from DataModel.Model import Model
from View.PyQt5GeneratedUis.ListOfPatientsView import UiListOfPatients
from Controller import MyListOfPatientsViewController


class MyListOfPatients(QtWidgets.QWidget):

    def __init__(self, model: Model, controller: MyListOfPatientsViewController):
        super().__init__()

        self._model = model
        self._controller = controller
        self._ui = UiListOfPatients()
        self._ui.setupUi(self)
        self.load_list()
        self._ui.showMonitoredPatientButton.clicked.connect(self.show_monitored_patients)
        self._controller.list_of_patients_finished.connect(self.hide)

    @pyqtSlot()
    def show_monitored_patients(self):
        self._controller.show_monitored_patients()

    def load_list(self):

        default_list_item = QtWidgets.QListWidgetItem()

        for patient in self._model._list_of_patients:
            patient_list_item = QtWidgets.QWidget()
            patient_list_item_label = QtWidgets.QLabel(patient.name)
            patient_list_item_button = QtWidgets.QPushButton("Monitor")
            patient_list_item_layout = QtWidgets.QHBoxLayout()
            patient_list_item_layout.addWidget(patient_list_item_label)
            patient_list_item_layout.addWidget(patient_list_item_button)
            patient_list_item_layout.addStretch()

            patient_list_item_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
            patient_list_item.setLayout(patient_list_item_layout)

            default_list_item.setSizeHint(patient_list_item.sizeHint())

            self._ui.allPatientListWidget.addItem(default_list_item)
            self._ui.allPatientListWidget.setItemWidget(default_list_item, patient_list_item)


    def update(self, subject_state):
        print("hello")
