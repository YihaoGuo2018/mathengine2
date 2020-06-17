from problem.Problem import Problem
from problem.CharacterList import CharacterList
from problem.Character import Character
from problem.SituationList import SituationList
from problem.Situation import Situation

from process_data.ProcessedData import ProcessedData
from process_data.ProcessedStep import ProcessedStep

from process_data.ProcessData import process_data
from database_pkg.CreatRawData import get_raw_data


def build_problem(processed_data=ProcessedData()):
    out_problem = Problem(processed_data.get_processed_problem_data().get_name(), build_situation_list(processed_data.get_processed_step_data_list()) )
    return out_problem


def build_situation_list(tmp_processed_step_list=[ProcessedStep()]):
    out_situation_list = SituationList()
    for processed_step in tmp_processed_step_list:
        out_situation_list.add_situation(build_situation(processed_step))
    return out_situation_list


def build_situation(tmp_processed_step=ProcessedStep()):
    out_situation = Situation()
    out_situation.set_name(tmp_processed_step.get_name())
    if tmp_processed_step.get_finish() == 2:
        out_situation.set_end()
    else:
        out_situation.cancel_end()
    out_situation.set_step(tmp_processed_step.get_step_number())
    if tmp_processed_step.get_type() == 1:
        out_situation.set_right()
    elif tmp_processed_step.get_type() == 2:
        out_situation.set_wrong()
    out_situation.set_character_list(build_character_list(tmp_processed_step.get_format()))
    out_situation.set_feedback(tmp_processed_step.get_feedback())

    return out_situation


def build_character_list(step_format=[]):
    out_character_list = CharacterList()
    out_character_list.set_easy_see(" ".join(step_format))
    for part in step_format:
        tmp_character = Character()
        tmp_character.set_content(part)
        out_character_list.add_character(tmp_character)

    return out_character_list


