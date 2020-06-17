import database_pkg.database as database
from database_pkg.RawData import RawData
from database_pkg.RawProblemData import RawProblemData
from database_pkg.RawSLParameter import RawSLParameter
from database_pkg.RawStep import RawStep


def get_raw_data(problem_id=1):
    tmp_raw_problem_data = get_raw_problem_data(problem_id)
    tmp_raw_sl_parameter = get_raw_sl_parameter_list(problem_id)
    tmp_raw_step_data = get_raw_step_list(problem_id)
    tmp_raw_data = RawData(tmp_raw_problem_data, tmp_raw_sl_parameter, tmp_raw_step_data)
    return tmp_raw_data


def get_raw_problem_data(problem_id=1):
    problem_data = database.get_problem(problem_id)
    if problem_data is None:
        print("warning  !!! get_raw_problem_data")
        return None

    tmp_problem_id = problem_data["problem_id"]
    tmp_name = problem_data["name"]
    tmp_description = problem_data["description"]
    tmp_parameter_number = problem_data["parameter_number"]
    tmp_stat_format = problem_data["start_format"]

    tmp_raw_problem_data = RawProblemData(tmp_problem_id, tmp_name, tmp_description, tmp_parameter_number,
                                          tmp_stat_format)

    return tmp_raw_problem_data


def get_raw_sl_parameter_list(problem_id=1):
    tmp_raw_sl_parameter_list = []

    sl_parameter_list = database.get_sl_parameter_list(problem_id)
    if sl_parameter_list is None:
        print("warning !!! get_raw_sl_parameter")

    for sl_parameter in sl_parameter_list:
        tmp_parameter_id = sl_parameter["parameter_id"]
        tmp_problem_id = sl_parameter["problem_id"]
        tmp_parameter_format = sl_parameter["parameter_format"]
        tmp_raw_sl_parameter = RawSLParameter(tmp_parameter_id, tmp_problem_id, tmp_parameter_format)
        tmp_raw_sl_parameter_list.append(tmp_raw_sl_parameter)

    return tmp_raw_sl_parameter_list


def get_raw_step_list(problem_id=1):
    tmp_raw_step_list = []

    raw_step_list = database.get_step_list(problem_id)
    if raw_step_list is None:
        print("warning !!! get_raw_step_list")

    for raw_step in raw_step_list:
        tmp_step_id = raw_step["step_id"]
        tmp_problem_id = raw_step["problem_id"]
        tmp_name = raw_step["name"]
        tmp_feedback = raw_step["feedback"]
        tmp_step_number = raw_step["step_number"]
        tmp_type = raw_step["type"]
        tmp_finish = raw_step["finish"]
        tmp_step_format = raw_step["step_format"]
        tmp_raw_step = RawStep(tmp_step_id, tmp_problem_id, tmp_name, tmp_feedback, tmp_step_number, tmp_type,
                               tmp_finish, tmp_step_format)

        tmp_raw_step_list.append(tmp_raw_step)

    return tmp_raw_step_list


# tmp = get_raw_data(1)
# a = 1