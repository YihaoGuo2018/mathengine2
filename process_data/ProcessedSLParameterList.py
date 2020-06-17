from process_data import ProcessedSLParameter


class ProcessedSLParameterList:
    def __init__(self):
        self.parameter_list = []

    def add_parameter(self, parameter):
        if type(parameter) == ProcessedSLParameter.ProcessedSLParameter:
            self.parameter_list.append(parameter)

    def get_value(self, parameter_id):
        for parameter in self.parameter_list:
            if parameter.get_id() == parameter_id:
                return parameter.get_value()
        return None