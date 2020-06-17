from database_pkg.RawData import RawData
from database_pkg.RawProblemData import RawProblemData
from database_pkg.RawSLParameter import RawSLParameter
from database_pkg.RawStep import RawStep
from database_pkg.CreatRawData import get_raw_data

from process_data.ProcessedData import ProcessedData
from process_data.ProcessedProblem import ProcessedProblem
from process_data.ProcessedFLParameterList import ProcessedFLParameterList
from process_data.ProcessedFLParameter import ProcessedFLParameter
from process_data.ProcessedSLParameterList import ProcessedSLParameterList
from process_data.ProcessedSLParameter import ProcessedSLParameter
from process_data.ProcessedStep import ProcessedStep


def process_raw_problem_data(raw_problem_data=RawProblemData()):
    tmp_processed_problem_data = ProcessedProblem()

    tmp_processed_problem_data.set_name(raw_problem_data.get_name())
    tmp_processed_problem_data.set_description(raw_problem_data.get_description())
    tmp_processed_problem_data.set_parameters(raw_problem_data.get_parameter_number())

    return tmp_processed_problem_data


def make_fl_parameters(parameters=[]):
    tmp_processed_fl_parameter_list = ProcessedFLParameterList()
    for id in range(len(parameters)):
        tmp_processed_fl_parameter_list.add_parameter(ProcessedFLParameter(id + 1, parameters[id]))
    return tmp_processed_fl_parameter_list


def make_sl_parameters(raw_sl_parameter_list=RawSLParameter(), processed_fl_parameter_list=[]):
    tmp_processed_sl_parameter_list = ProcessedSLParameterList()
    for i in range(len(raw_sl_parameter_list)):
        tmp_processed_sl_parameter = ProcessedSLParameter()
        tmp_raw_sl_parameter = raw_sl_parameter_list[i]

        save_value = 0

        sl_raw_format = tmp_raw_sl_parameter.get_format()
        sl_separate_format = sl_raw_format.split(",")

        save_id = int(sl_separate_format[0][1:])
        value_1 = sl_separate_format[1]
        value_2 = sl_separate_format[3]
        symbol = sl_separate_format[2]

        tmp_value_1, tmp_value_2 = 0, 0

        if value_1[0] == "$":
            tmp_value_1 = processed_fl_parameter_list.get_value(int(value_1[1:]))
            if tmp_value_1 is None:
                print("warning !!! can't find")
                break
        elif value_1[0] == "#":
            tmp_value_1 = tmp_processed_sl_parameter_list.get_value(int(value_1[1:]))
            if tmp_value_1 is None:
                print("warning !!! can't find")
                break
        else:
            tmp_value_1 = int(value_1)

        if value_2[0] == "$":
            tmp_value_2 = processed_fl_parameter_list.get_value(int(value_2[1:]))
            if tmp_value_2 is None:
                print("warning !!! can't find")
                break
        elif value_2[0] == "#":
            tmp_value_2 = tmp_processed_sl_parameter_list.get_value(int(value_2[1:]))
            if tmp_value_2 is None:
                print("warning !!! can't find")
                break
        else:
            tmp_value_2 = int(value_2)

        if symbol == "+":
            save_value = tmp_value_1 + tmp_value_2
        elif symbol == "-":
            save_value = tmp_value_1 - tmp_value_2
        elif symbol == "*":
            save_value = tmp_value_1 * tmp_value_2
        elif symbol == "/":
            save_value = tmp_value_1 / tmp_value_2

        tmp_processed_sl_parameter.set_id(save_id)
        tmp_processed_sl_parameter.set_value(save_value)
        tmp_processed_sl_parameter_list.add_parameter(tmp_processed_sl_parameter)

    return tmp_processed_sl_parameter_list


def make_processed_step_data(raw_step_data_list=[RawStep()], processed_fl_parameter_list=ProcessedFLParameterList(),
                             processed_sl_parameter_list=ProcessedSLParameterList()):
    processed_step_data_list = []
    for i in range(len(raw_step_data_list)):
        tmp_raw_step_data = raw_step_data_list[i]
        tmp_name = tmp_raw_step_data.get_name()
        tmp_feedback = tmp_raw_step_data.get_feedback()
        tmp_step_number = tmp_raw_step_data.get_step_number()
        tmp_step_type = tmp_raw_step_data.get_type()
        tmp_finish = tmp_raw_step_data.get_finish()
        tmp_format = tmp_raw_step_data.get_format().split(",")

        step_format = []

        for part in tmp_format:
            if part[0] == "#":
                tmp_value = processed_sl_parameter_list.get_value(int(part[1:]))
                step_format.append(str(tmp_value))
            elif part[0] == "$":
                tmp_value = processed_fl_parameter_list.get_value(int(part[1:]))
                step_format.append(str(tmp_value))
            else:
                step_format.append(part)

        processed_step_data = ProcessedStep(tmp_name, tmp_feedback, tmp_step_number, tmp_step_type, tmp_finish, step_format)

        processed_step_data_list.append(processed_step_data)
    return processed_step_data_list


def process_data(raw_data=RawData(), parameters=[]):
    if type(raw_data) != RawData:
        print("warning the processed data type not RawData")
        return None

    tmp_raw_problem_data = raw_data.get_raw_problem_data()
    tmp_raw_sl_parameter_list = raw_data.get_raw_sl_parameter_list()
    tmp_raw_step_data_list = raw_data.get_raw_step_data_list()

    tmp_processed_problem_data = process_raw_problem_data(tmp_raw_problem_data)
    tmp_processed_fl_parameter_list = make_fl_parameters(parameters)
    tmp_processed_sl_parameter_list = make_sl_parameters(tmp_raw_sl_parameter_list, tmp_processed_fl_parameter_list)
    tmp_processed_step_data_list = make_processed_step_data(tmp_raw_step_data_list, tmp_processed_fl_parameter_list,
                                                            tmp_processed_sl_parameter_list)

    processed_data = ProcessedData(tmp_processed_problem_data, tmp_processed_fl_parameter_list,
                                   tmp_processed_sl_parameter_list, tmp_processed_step_data_list)

    return processed_data


# tmp = get_raw_data(1)
# # tmp2 = process_data(tmp, [3, 4, 10, 20])
# # tmp = 1