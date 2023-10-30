class Taxi:
    def __init__(self, id) -> None:
        self.id = id

    def toString(self, name, avto_model, avto_raqam):
        self.name = name
        self.avto_model = avto_model
        self.avto_raqam = avto_raqam
        return self.name, self.avto_model, self.avto_raqam