

class ProcessedProblem:

    def __init__(self, name="Default ProcessedProblem", description="", parameter_number=0):
        self.set_name(name)
        self.set_description(description)
        self.set_parameters(parameter_number)

    def set_parameters(self, parameter_number):
        if type(parameter_number) == int:
            self.ParameterNumber = parameter_number
        else:
            print(" warning !!!  ProcessedProblemData.set_parameter_number type error")

    def get_parameter_number(self):
        return self.ParameterNumber

    def set_name(self, name):
        if type(name) == str:
            self.Name = name
        else:
            print("warning !!! ProcessedProblemData.set_name type error")

    def get_name(self):
        return self.Name

    def set_description(self, description):
        if type(description) == str:
            self.Description = description
        else:
            print("warning !!! ProcessedProblemData.set_description type error")

    def get_description(self):
        return self.Description
