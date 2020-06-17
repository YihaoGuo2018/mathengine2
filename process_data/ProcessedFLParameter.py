
class ProcessedFLParameter:
    def __init__(self, parameter_id, value):
        self.ParameterId = 0
        self.ParameterValue = 0
        self.set_id(parameter_id)
        self.set_value(value)

    def set_value(self, value):
        if type(value) == int:
            self.ParameterValue = value
        else:
            print("warning !!! ProcessedFLParameter.set_value")

    def get_value(self):
        return self.ParameterValue

    def set_id(self, parameter_id):
        if type(parameter_id) == int:
            self.ParameterId = parameter_id
        else:
            print("warning !!! ProcessedFLParameter.set_id ")

    def get_id(self):
        return self.ParameterId

