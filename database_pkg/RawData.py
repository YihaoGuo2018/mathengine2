from database_pkg import RawStep, RawSLParameter, RawProblemData


class RawData:

    def __init__(self, raw_problem_data=RawProblemData.RawProblemData(), raw_sl_parameter_list=[], raw_step_data_list=[]):
        self.set_raw_problem_data(raw_problem_data)
        self.set_raw_sl_parameter_list(raw_sl_parameter_list)
        self.set_raw_step_data_list(raw_step_data_list)

    def set_raw_problem_data(self, raw_problem_data):
        if type(raw_problem_data) == RawProblemData.RawProblemData:
            self.RawProblemData = raw_problem_data
        else:
            print("warning ! set_raw_problem_data has a type problem")

    def get_raw_problem_data(self):
        return self.RawProblemData

    def add_raw_sl_parameter(self, raw_sl_parameter):
        if type(raw_sl_parameter) == RawSLParameter.RawSLParameter:
            self.RawSLParameterList.append(raw_sl_parameter)
        else:
            print("warning ! add_raw_sl_parameter has a type problem")

    def set_raw_sl_parameter_list(self, raw_sl_parameter_list):
        if type(raw_sl_parameter_list) != list:
            print("warning !!! set_raw_sl_parameter_list")
            return
        self.RawSLParameterList = []
        for raw_sl_parameter in raw_sl_parameter_list:
            self.add_raw_sl_parameter(raw_sl_parameter)

    def get_raw_sl_parameter_list(self):
        return self.RawSLParameterList

    def add_raw_step_data(self, raw_step_data):
        if type(raw_step_data) == RawStep.RawStep:
            self.RawStepDataList.append(raw_step_data)
        else:
            print("warning ! add_raw_step_data has a type problem")

    def set_raw_step_data_list(self, raw_step_data_list):
        if type(raw_step_data_list) != list:
            print("warning !!! set_raw_step_data_list")
            return
        self.RawStepDataList = []
        for raw_step_data in raw_step_data_list:
            self.add_raw_step_data(raw_step_data)

    def get_raw_step_data_list(self):
        return self.RawStepDataList
