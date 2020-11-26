import types


class Connection:
    def method(self):
        return "connection method"

class DataModel:
    """
    docstring
    """
    def __init__(self):
        self.connection = Connection()

    def data_model_method(self,input):
        self.connection.method()
        return "data_model_method"

datamodel = DataModel()

if __name__ == "__main__":
    a = DataModel()
    a.connection.method()