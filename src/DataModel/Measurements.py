from DataModel.Cholesterol import Cholesterol


class Measurements:

    def __init__(self, cholesterol: Cholesterol = None):

        assert type(cholesterol) is Cholesterol or cholesterol is None, "cholesterol can only be either an instance " \
                                                                        "of Cholesterol class or None (when there's " \
                                                                        "no data) but it is of type " + \
                                                                        str(type(cholesterol))

        self.__cholesterol = cholesterol

    def get_cholesterol(self):
        return self.__cholesterol

    def set_cholesterol(self, cholesterol: Cholesterol):

        assert type(cholesterol) is Cholesterol, "cholesterol should be an instance of Cholesterol class but it is " \
                                                 "of type " + str(type(cholesterol))

        self.__cholesterol = cholesterol

    def get_summary(self):

        summary = "Cholesterol: " + self.__cholesterol.get_cholesterol_description()

        return summary