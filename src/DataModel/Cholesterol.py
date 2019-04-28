class Cholesterol:

    def __init__(self, value: float, unit: str):

        assert type(value) is float, "Cholesterol value should be a float but is of type " + str(type(value))
        assert type(unit) is str, "Cholesterol unit should be a string but is of type " + str(type(unit))

        assert value > 0, "Cholesterol needs to be positive but is " + str(value)
        assert unit == "mg/dL" or unit == "mmol/L", "Cholesterol should be measured using either mg/dL or mmol/L but " \
                                                    "the input unit is " + unit

        self.__value = value
        self.__unit = unit

    def get_value(self):
        return self.__value

    def set_value(self, value: float):
        assert type(value) is float, "Cholesterol value should be a float but is of type " + str(type(value))
        assert value > 0, "Cholesterol needs to be positive but is " + str(value)

        self.__value = value

    def set_unit(self, unit: str):
        assert type(unit) is str, "Cholesterol unit should be a string but is of type " + str(type(unit))
        assert unit == "mg/dL" or unit == "mmol/L", "Cholesterol should be measured using either mg/dL or mmol/L but " \
                                                    "the input unit is " + unit

        self.__unit = unit

    def get_cholesterol_description(self):
        return str(self.__value) + " " + self.__unit
