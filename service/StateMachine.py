from problem.Problem import Problem
from service.State import State
from problem.CharacterList import CharacterList
from problem.Situation import Situation
from service.Result import Result
from service.State import State
from problem.DefaultSituation import DefaultSituation
import copy


class StateMachine:

    def __init__(self):
        self.State_Machine_id = 0
        self.Problem = Problem()
        self.State = State()

    def set_problem(self, problem=Problem()):
        if type(problem) == Problem:
            self.Problem = problem
        else:
            print("warning !!! StateMachine. set_problem")

    def get_problem(self):
        return self.Problem

    def set_state(self):
        None

        
    def change_state(self, character_list=CharacterList()):
        old_state = copy.deepcopy(self.State)
        situation_list = self.Problem.get_situation_list()
        situation = situation_list.find_situation(character_list)
        if situation is not None:
            if situation.get_step() > self.State.get_step() and situation.is_right():
                self.State.set_step(situation.get_step())
        else:
            situation = DefaultSituation()

        return self.make_result(old_state, self.State, situation)

    def make_result(self, old_state=State(), new_state=State(), situation=Situation()):
        out_result = Result()
        if old_state.get_step() < new_state.get_step() and situation.is_right():
            out_result.set_right()
        else:
            out_result.set_wrong()
        out_result.set_step(new_state.get_step())
        out_result.set_feedback(situation.get_feedback())
        return out_result


