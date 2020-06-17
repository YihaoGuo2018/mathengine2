
class RawSLParameter:

    def __init__(self, parameter_id=0, problem_id=0, parameter_format=""):
        self.set_id(parameter_id)
        self.set_problem_id(problem_id)
        self.set_format(parameter_format)

    def set_id(self, parameter_id):
        if type(parameter_id) == int:
            self.ParameterId = parameter_id
        else:
            print("warning !!! RawSLParameter.set_id type error")

    def get_id(self):
        return self.ParameterId

    def set_problem_id(self, problem_id):
        if type(problem_id) == int:
            self.ProblemId = problem_id
        else:
            print("warning !!! RawSLParameter.set_problem_id type error")

    def get_problem_id(self):
        return self.ProblemId

### 需要添加格式检测

    def set_format(self, parameter_format = ""):
        if type(parameter_format) == str:
            self.ParameterFormat = parameter_format.replace(" ", "")
        else:
            print("warning !!! RawSLParameter.set_format type error")

    def get_format(self):
        return self.ParameterFormat
