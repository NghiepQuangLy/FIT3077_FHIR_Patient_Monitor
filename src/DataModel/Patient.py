class Patient:

    def __init__(self, id: str, name: str):

        assert type(id) is str, "patient id should be a string but is " + str(type(id))
        assert type(name) is str, "patient name should be a string but is " + str(type(name))

        self.id = id
        self.name = name
