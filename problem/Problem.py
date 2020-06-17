from problem.SituationList import SituationList


class Problem:

    def __init__(self, name="default_problem", situations=SituationList()):
        self.Name = name
        self.Situation_List = situations


        # self.Parameter_number = parameter_number
        # self.Parameters = parameters

    def get_situation_list(self):
        return self.Situation_List
