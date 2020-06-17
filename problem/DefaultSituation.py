from problem.CharacterList import CharacterList


class DefaultSituation:
    def __init__(self):
        self.Situation_Name = "default_situation"
        self.End = 0  # 0不是 1是
        self.Step_number = 0  # 从1开始
        self.Right_step = 0
        self.Wrong_step = 1

        self.Feedback = ""

    def get_feedback(self):
        return self.Feedback

    def get_name(self):
        return self.Situation_Name

    def is_right(self):
        return self.Right_step

    def is_wrong(self):
        return self.Wrong_step

    def get_step(self):
        return self.Step_number

    def is_end(self):
        return self.End
