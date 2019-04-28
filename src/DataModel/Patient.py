class Patient:

    def __init__(self, id: str, name: str):

        if type(id) is not str:
            raise TypeError("id should be an string but is " + str(type(id)))

        if type(name) is not str:
            raise TypeError("name should be a string but is " + str(type(name)))

        self.id = id
        self.name = name
