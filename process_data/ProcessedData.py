# from process_data import ProcessedStep, ProcessedFLParameterList, ProcessedProblem, ProcessedSLParameterList
from process_data.ProcessedFLParameterList import ProcessedFLParameterList
from process_data.ProcessedProblem import ProcessedProblem
from process_data.ProcessedSLParameterList import ProcessedSLParameterList
from process_data.ProcessedStep import ProcessedStep


class ProcessedData:

    def __init__(self, processed_problem_data=ProcessedProblem(),
                 processed_fl_parameter_list=ProcessedFLParameterList(),
                 processed_sl_parameter_list=ProcessedSLParameterList(),
                 processed_step_data_list=[]):
        self.set_processed_problem_data(processed_problem_data)
        self.set_processed_fl_parameter_list(processed_fl_parameter_list)
        self.set_processed_sl_parameter_list(processed_sl_parameter_list)
        self.set_processed_step_data_list(processed_step_data_list)

    def set_processed_problem_data(self, processed_problem_data):
        if type(processed_problem_data) == ProcessedProblem:
            self.ProcessedProblemData = processed_problem_data
        else:
            print("warning ! set_Processed_problem_data has a type problem")

    def get_processed_problem_data(self):
        return self.ProcessedProblemData

    def set_processed_sl_parameter_list(self, processed_sl_parameter_list):
        if type(processed_sl_parameter_list) == ProcessedSLParameterList:
            self.ProcessedSLParameterList = processed_sl_parameter_list
        else:
            print("warning !")

    def get_processed_sl_parameter_list(self):
        return self.ProcessedSLParameterList

    def set_processed_fl_parameter_list(self, processed_fl_parameter_list):
        if type(processed_fl_parameter_list) == ProcessedFLParameterList:
            self.ProcessedFLParameterList = processed_fl_parameter_list
        else:
            print("warning !")

    def get_processed_fl_parameter_list(self):
        return self.ProcessedFLParameterList

    def add_processed_step_data(self, processed_step_data):
        if type(processed_step_data) == ProcessedStep:
            self.ProcessedStepDataList.append(processed_step_data)
        else:
            print("warning ! add_Processed_step_data has a type problem")

    def set_processed_step_data_list(self, processed_step_data_list):
        if processed_step_data_list is None:
            print("warning !!! set_processed_step_data_list")
            return
        self.ProcessedStepDataList = []
        for processed_step_data in processed_step_data_list:
            self.add_processed_step_data(processed_step_data)

    def get_processed_step_data_list(self):
        return self.ProcessedStepDataList
