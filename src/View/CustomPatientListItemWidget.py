from PyQt5 import QtWidgets


class CustomPatientListItemWidget(QtWidgets.QWidget):

    def __init__(self, patient_name: str, action: str, callback_func, unique_id: str):
        super().__init__()
        patient_list_item_label = QtWidgets.QLabel(patient_name)
        patient_list_item_button = QtWidgets.QPushButton(action)
        patient_list_item_button.clicked.connect(callback_func)
        patient_list_item_button.setObjectName(unique_id)
        patient_list_item_layout = QtWidgets.QHBoxLayout()
        patient_list_item_layout.addWidget(patient_list_item_label)
        patient_list_item_layout.addWidget(patient_list_item_button)
        patient_list_item_layout.addStretch()

        patient_list_item_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.setLayout(patient_list_item_layout)
