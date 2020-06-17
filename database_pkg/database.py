import pymysql

from database_pkg import database_config

address = database_config.address
user = database_config.user
password = database_config.password
database = database_config.database


def get_problem(problem_id=1):
    problem = []
    db = pymysql.connect(address, user, password, database)
    cursor = db.cursor()
    sentence = "SELECT * FROM test_database.problem where ID = {};".format(problem_id)
    cursor.execute(sentence)
    data = cursor.fetchone()
    if data:
        problem = {"problem_id": data[0], "name": data[1], "description": data[2],
                   "parameter_number": data[3], "start_format": data[4]}
    db.close()
    return problem


def get_sl_parameter_list(problem_id=1):
    sl_parameter_list = []
    db = pymysql.connect(address, user, password, database)
    cursor = db.cursor()
    sentence = "SELECT * FROM test_database.second_level_parameter where problem_ID = {};".format(problem_id)
    cursor.execute(sentence)
    data_set = cursor.fetchall()
    for data in data_set:
        tmp_data = {"parameter_id": data[0], "problem_id": data[1], "parameter_format": data[2]}
        sl_parameter_list.append(tmp_data.copy())
    db.close()
    return sl_parameter_list


def get_step_list(problem_id=1):
    steps = []
    db = pymysql.connect(address, user, password, database)
    cursor = db.cursor()
    sentence = "SELECT * FROM test_database.step_info where problem_ID = {}".format(problem_id)
    cursor.execute(sentence)
    data_set = cursor.fetchall()
    for data in data_set:
        tmp_data = {"step_id": data[0], "problem_id": data[1], "name": data[2], "feedback": data[3], "step_number": data[4],
                    "type": data[5], "finish": data[6],
                    "step_format": data[7]}
        steps.append(tmp_data.copy())
    db.close()
    return steps


# print(get_problem(30))
# print(get_sl_parameters(30))
# print(get_steps(30))
