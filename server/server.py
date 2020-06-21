from flask import Flask, request
from flask_cors import *
import json

from database_pkg.CreatRawData import get_raw_data
from process_data.ProcessData import process_data
from problem.BuildProblem import build_problem
from service.StateMachine import StateMachine
from service.Process_input import process_text
from service.State import State

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/MathEngine/1', methods=['POST'])
def math_engine():

    problem_id = request.get_json()["problem_id"]
    parameter_number = request.get_json()["parameter_number"]
    tmppp = request.get_json()["parameter_list"]
    parameter_list = tmppp.split(",")
    for i in range(parameter_number):
        parameter_list[i] = int(parameter_list[i])


    old_step = request.get_json()["old_step"]
    answer = request.get_json()["answer"]

    raw_data = get_raw_data(problem_id)
    processed_data = process_data(raw_data,parameter_list)
    problem = build_problem(processed_data)

    answer = process_text(answer)

    state_machine = StateMachine()
    state_machine.set_problem(problem)
    new_state = State()
    new_state.set_step(old_step)
    state_machine.set_state(new_state)

    result = state_machine.change_state(answer)

    out_result = {"right": result.is_right(), "wrong": result.is_wrong(), "new_step": result.get_step(),
                  "feedback": result.get_feedback(), "is_end": result.is_end()}

    out_result = json.dumps(out_result)
    return out_result

if __name__ == '__main__':
    app.run()