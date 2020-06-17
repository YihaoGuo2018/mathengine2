
class RawProblemData:
    def __init__(self, problem_id=0, name="DefaultRawProblemData", description="", parameter_number=0, start_format=""):
        self.set_id(problem_id)
        self.set_name(name)
        self.set_parameter_number(parameter_number)
        self.set_description(description)
        self.set_start_format(start_format)

    def set_parameter_number(self, parameter_number):
        if type(parameter_number) == int:
            self.ParameterNumber = parameter_number
        else:
            print(" warning !!!  RawProblemData.set_parameter_number type error")

    def get_parameter_number(self):
        return self.ParameterNumber

    def set_id(self, problem_id):
        if type(problem_id) == int:
            self.Problem_Id = problem_id
        else:
            print("warning !!! RawProblemData.set_id type error")

    def get_id(self):
        return self.Problem_Id

    def set_name(self, name):
        if type(name) == str:
            self.Name = name
        else:
            print("warning !!! RawProblemData.set_name type error")

    def get_name(self):
        return self.Name

    def set_description(self, description):
        if type(description) == str:
            self.Description = description
        else:
            print("warning !!! RawProblemData.set_description type error")

    def get_description(self):
        return self.Description

### 需要添加格式检测

    def set_start_format(self, start_format):
        if type(start_format) == str:
            self.StartFormat = start_format.replace(" ", "")
        else:
            print(" warning !!! RawProblemData.set_start_format type error")

    def get_start_format(self):
        return self.StartFormat
