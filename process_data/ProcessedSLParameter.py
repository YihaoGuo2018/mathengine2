
class ProcessedSLParameter:
    def __init__(self):
        self.ParameterId = 0
        self.ParameterValue = 0

    def set_value(self, parameter_value):
        if type(parameter_value) == int:
            self.ParameterValue = parameter_value
        else:
            print("warning  !!! ProcessedSLParameter.set_value")

    def get_value(self):
        return self.ParameterValue

    def set_id(self, parameter_id):
        if type(parameter_id) == int:
            self.ParameterId = parameter_id
        else:
            print("warning !!!  ProcessedSLParameter.set_id ")

    def get_id(self):
        return self.ParameterId





    # def __init__(self, id, problem_id, format):
    #     self.set_id(id)
    #     self.set_problem_id(problem_id)
    #     self.set_format(format)
    #
    # def set_parameters(self, parameter_number, parameters):
    #     if type(parameter_number) == int and type(parameters) == list and len(parameters) == parameter_number:
    #         self.ParameterNumber = parameter_number
    #         self.Parameters = parameters[:]
    #     else:
    #         print(" warning !!!  ProcessedProblemData.set_parameter_number type error")
    #
    # def get_parameters(self):
    #     return self.Parameters
    #
    # def get_parameter_number(self):
    #
    # def set_id(self, id):
    #     if type(id) == int:
    #         self.Id = id
    #     else:
    #         print("warning !!! ProcessedSLParameter.set_id type error")
    #
    # def get_id(self):
    #     return self.Id
    #
    # def set_problem_id(self, problem_id):
    #     if type(problem_id) == int:
    #         self.ProblemId = problem_id
    #     else:
    #         print("warning !!! ProcessedSLParameter.set_problem_id type error")
    #
    # def get_problem_id(self):
    #     return self.ProblemId
    #
    # def set_format(self, format):
    #     if type(format) == str:
    #         self.Format = format
    #     else:
    #         print("warning !!! ProcessedSLParameter.set_format type error")
    #
    # def get_format(self):
    #     return self.Format