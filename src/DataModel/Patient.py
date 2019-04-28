from DataModel.MedicalData import MedicalData


class Patient:

    def __init__(self, id: str, name: str, medical_data: MedicalData = None):

        assert type(id) is str, "patient id should be a string but is " + str(type(id))
        assert type(name) is str, "patient name should be a string but is " + str(type(name))
        assert type(medical_data) is MedicalData or medical_data is None, \
            "medical data should be an instance of MedicalData class but is of type " + str(type(medical_data))

        self.id = id
        self.name = name
        self.medical_data = medical_data

    def set_medical_data(self, medical_data: MedicalData):

        assert type(medical_data) is MedicalData, "medical data should be an instance of MedicalData class but is of" \
                                                  "type " + str(type(medical_data))

        self.medical_data = medical_data
