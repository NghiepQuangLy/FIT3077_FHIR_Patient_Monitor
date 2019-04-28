from DataModel.Measurements import Measurements


class MedicalData:

    def __init__(self, measurements: Measurements = None):

        assert type(measurements) is Measurements or measurements is None, "recorded measurements can only be either " \
                                                                           "an instance of Measurements class or None" \
                                                                           " (when patient has no measurements) but " \
                                                                           "it is " + str(type(measurements))
        self.__measurements = measurements

    def get_measurements(self):
        return self.__measurements

    def set_measurements(self, measurements: Measurements):

        assert type(measurements) is Measurements, "recorded measurements should be an instance of Measurements class" \
                                                   "but it is " + str(type(measurements))

        self.__measurements = measurements
