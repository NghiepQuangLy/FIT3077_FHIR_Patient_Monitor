from abc import ABC, abstractmethod


class Observation(ABC):

    _name: str
    _value: float
    _unit: str

    def __init__(self, name: str, value: float, unit: str):
        assert type(name) is str, "Observation name should be a string but it is of type " + str(type(name))
        assert type(value) is float, "Observation value should be a float but is of type " + str(type(value))
        assert type(unit) is str, "Observation unit should be a string but is of type " + str(type(unit))

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit

    @name.setter
    @abstractmethod
    def name(self, name: str):
        pass

    @value.setter
    @abstractmethod
    def value(self, value: float):
        pass

    @unit.setter
    @abstractmethod
    def unit(self, unit: str):
        pass

    def get_description(self):
        return str(self._name) + ": " + str(self._value) + " " + str(self._unit)