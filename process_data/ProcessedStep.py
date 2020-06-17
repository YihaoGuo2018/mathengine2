class ProcessedStep:

    def __init__(self, name="", feedback="", step_number=0, step_type=0, finish=0, step_format=[]):
        self.set_name(name)
        self.set_feedback(feedback)
        self.set_step_number(step_number)
        self.set_type(step_type)
        self.set_finish(finish)
        self.set_format(step_format)

    def set_name(self, name):
        if type(name) == str:
            self.Name = name
        else:
            print("warning !!! ProcessedStepData.set_name type error")

    def get_name(self):
        return self.Name

    def set_feedback(self, feedback):
        if type(feedback) == str:
            self.Feedback = feedback
        else:
            print("warning !!! ProcessedStepData.set_feedback type error")

    def get_feedback(self):
        return self.Feedback

    def set_step_number(self, step_number):
        if type(step_number) == int:
            self.StepNumber = step_number
        else:
            print("warning !!! ProcessedStepData.set_step_number type error")

    def get_step_number(self):
        return self.StepNumber

    def set_type(self, step_type):
        if type(step_type) == int:
            self.StepType = step_type
        else:
            print("warning !!! ProcessedStepData.set_type type error")

    def get_type(self):
        return self.StepType

    def set_finish(self, finish):
        if type(finish) == int:
            self.Finish = finish
        else:
            print("warning !!! ProcessedStepData.set_finish finish error")

    def get_finish(self):
        return self.Finish

    def set_format(self, step_format):
        if type(step_format) == list:
            self.Format = step_format[:]
        else:
            print("warning !!! ProcessedStepData.set_format format error")

    def get_format(self):
        return self.Format
