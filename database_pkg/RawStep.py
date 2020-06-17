
class RawStep:

    def __init__(self, step_id=0, problem_id=0, name="", feedback="", step_number=0, step_type=0, finish=0, step_format=""):
        self.set_id(step_id)
        self.set_problem_id(problem_id)
        self.set_name(name)
        self.set_feedback(feedback)
        self.set_step_number(step_number)
        self.set_type(step_type)
        self.set_finish(finish)
        self.set_format(step_format)

    def set_id(self, step_id):
        if type(step_id) == int:
            self.StepId = step_id
        else:
            print("warning !!! RawStepData.set_id type error")

    def get_id(self):
        return self.StepId

    def set_problem_id(self, problem_id):
        if type(problem_id) == int:
            self.ProblemId = problem_id
        else:
            print("warning !!! RawStepData.set_problem_id type error")

    def get_problem_id(self):
        return self.ProblemId

    def set_name(self, name):
        if type(name) == str:
            self.Name = name
        else:
            print("warning !!! RawStepData.set_name type error")

    def get_name(self):
        return self.Name

    def set_feedback(self, feedback):
        if type(feedback) == str:
            self.Feedback = feedback
        else:
            print("warning !!! RawStepData.set_feedback type error")

    def get_feedback(self):
        return self.Feedback

    def set_step_number(self, step_number):
        if type(step_number) == int:
            self.StepNumber = step_number
        else:
            print("warning !!! RawStepData.set_step_number type error")

    def get_step_number(self):
        return self.StepNumber

    def set_type(self, step_type):
        if type(step_type) == int:
            self.Type = step_type
        else:
            print("warning !!! RawStepData.set_type type error")

    def get_type(self):
        return self.Type

    def set_finish(self, finish):
        if type(finish) == int:
            self.Finish = finish
        else:
            print("warning !!! RawStepData.set_finish finish error")

    def get_finish(self):
        return self.Finish

# 需加格式检测

    def set_format(self, step_format):
        if type(step_format) == str:
            self.StepFormat = step_format.replace(" ", "")
        else:
            print("warning !!! RawStepData.set_format format error")

    def get_format(self):
        return self.StepFormat
