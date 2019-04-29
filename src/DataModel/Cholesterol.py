from DataModel.Observation import Observation


class Cholesterol(Observation):

    def __init__(self, name: str, value: float, unit: str):

        super().__init__(name, value, unit)

        assert value > 0, "Cholesterol needs to be positive but is " + str(value)
        assert unit == "mg/dL" or unit == "mmol/L", "Cholesterol should be measured using either mg/dL or mmol/L but " \
                                                    "the input unit is " + unit

        self._name = name
        self._value = value
        self._unit = unit

    @Observation.name.setter
    def name(self, name: str):
        assert type(name) is str, "Name of cholesterol must be of string type but it is " + str(type(name))
        self._name = name

    @Observation.value.setter
    def value(self, value: float):
        assert type(value) is float, "Value of cholesterol must be of float type but it is " + str(type(value))
        assert value > 0, "Cholesterol needs to be positive but is " + str(value)

        self._value = value

    @Observation.unit.setter
    def unit(self, unit: str):
        assert type(unit) is str, "Unit of cholesterol must be of string type but it is " + str(type(unit))
        assert unit == "mg/dL" or unit == "mmol/L", "Cholesterol should be measured using either mg/dL or mmol/L but " \
                                                    "the input unit is " + unit

        self._unit = unit

