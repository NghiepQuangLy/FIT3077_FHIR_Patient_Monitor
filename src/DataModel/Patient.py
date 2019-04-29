from DataModel.Observation import Observation


class Patient:

    def __init__(self, id: str, name: str, observations: {Observation} = {}):

        assert type(id) is str, "patient id should be a string but is " + str(type(id))
        assert type(name) is str, "patient name should be a string but is " + str(type(name))

        for observation in observations:
            assert issubclass(type(observations[observation]), Observation), "An observation must be an instance of " \
                                                                             "Observation class but it is of type " + \
                                                                             str(type(observation))

        self.id = id
        self.name = name
        self.observations = observations

    def set_medical_data(self, observations: {Observation}):

        if observations is None:
            raise Exception("observations can not be of None")

        for observation in observations:
            assert issubclass(type(observations[observation]), Observation), "An observation must be an instance of " \
                                                                             "Observation class but it is of type " + \
                                                                             str(type(observation))

        self.observations = observations

    def update_observations(self, observation: Observation):

        assert issubclass(type(observation), Observation), "An observation must be an instance of Observation " \
                                                           "class but it is of type " + str(type(observation))

        self.observations[observation.name] = observation
