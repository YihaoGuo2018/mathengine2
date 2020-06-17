from problem.CharacterList import CharacterList


class Situation:
    def __init__(self):
        self.Situation_Name = "default_situation"
        self.End = 0 # 0不是 1是
        self.Step_number = 0 #  从1开始
        self.Right_step = 0
        self.Wrong_step = 0
        self.Character_list = CharacterList()
        self.Feedback = ""
    def check_situation(self, tmp_character_list):
        if type(tmp_character_list) == CharacterList:
            if tmp_character_list == self.Character_list:
                return True
            else:
                return False
        else:
            print("warning !!! Situation.check_situation")

    def set_feedback(self, feedback):
        self.Feedback = feedback

    def get_feedback(self):
        return self.Feedback

    def set_character_list(self, character_list=CharacterList()):
        self.Character_list = character_list

    def get_character_list(self):
        return self.Character_list

    def set_name(self, name=""):
        self.Situation_Name = name

    def get_name(self):
        return self.Situation_Name


    def add_character(self, characters):
        self.Characters = characters

    def set_right(self):
        self.Right_step = 1
        self.Wrong_step = 0

    def set_wrong(self):
        self.Right_step = 0
        self.Wrong_step = 1

    def is_right(self):
        return self.Right_step

    def is_wrong(self):
        return self.Wrong_step

    def set_step(self, step_number):
        self.Step_number =  step_number

    def get_step(self):
        return self.Step_number

    def is_step(self, step_number):
        return self.Step_number == step_number

    def set_end(self):
        self.End = 1

    def cancel_end(self):
        self.End = 0

    def is_end(self):
        return self.End
