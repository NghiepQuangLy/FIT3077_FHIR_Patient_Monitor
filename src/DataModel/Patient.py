from DataModel.Observation import Observation


class Patient:

    def __init__(self, id: str, name: str, observations: {Observation} = {}):

        assert type(id) is str, "patient id should be a string but is " + str(type(id))
        assert type(name) is str, "patient name should be a string but is " + str(type(name))

        for observation in observations:
            assert issubclass(type(observations[observation]), Observation), "An observation must be an instance of " \
                                                                             "Observation class but it is of type " + \
                                                                             str(type(observation))

        self._id = id
        self._name = name
        self._observations = observations

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def observations(self):
        return self._observations

    def set_medical_data(self, observations: {Observation}):

        if observations is None:
            raise Exception("observations can not be of None")

        for observation in observations:
            assert issubclass(type(observations[observation]), Observation), "An observation must be an instance of " \
                                                                             "Observation class but it is of type " + \
                                                                             str(type(observation))

        self._observations = observations

    def update_observations(self, observation: Observation):

        assert issubclass(type(observation), Observation), "An observation must be an instance of Observation " \
                                                           "class but it is of type " + str(type(observation))

        self._observations[observation.name] = observation
