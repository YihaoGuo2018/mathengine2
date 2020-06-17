import problem.Situation


class SituationList:
    def __init__(self):
        self.Situation_List = []

    def add_situation(self, situation):
        self.Situation_List.append(situation)

    def find_situation(self, tmp_character_list):
        for situation in self.Situation_List:
            if situation.check_situation(tmp_character_list):
                return situation
        return None

