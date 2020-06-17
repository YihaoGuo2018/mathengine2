from process_data import ProcessedFLParameter


class ProcessedFLParameterList:
    def __init__(self):
        self.parameter_list = []

    def add_parameter(self, parameter):
        if type(parameter) == ProcessedFLParameter.ProcessedFLParameter:
            self.parameter_list.append(parameter)

    def get_value(self, parameter_id):
        for parameter in self.parameter_list:
            if parameter.get_id() == parameter_id:
                return parameter.get_value()
        return None

    def get_data(self):
        out = []
        for parameter in self.parameter_list:
            out.append([parameter.get_id(), parameter.get_value()])
        return out
