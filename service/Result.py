
class Result:
    def __init__(self):
        self.Id = 0
        self.Right_Answer = False
        self.Wrong_Answer = False
        self.New_step = 0
        self.Feedback = "your answer has a mistake here"
        self.IsEnd = False

    def set_end(self, end):
        self.IsEnd = end

    def is_end(self):
        return self.IsEnd

    def set_right(self):
        self.Right_Answer = True
        self.Wrong_Answer = False

    def set_wrong(self):
        self.Right_Answer = False
        self.Wrong_Answer = True

    def is_right(self):
        return self.Right_Answer

    def is_wrong(self):
        return self.Wrong_Answer

    def set_step(self, step):
        self.New_step = step

    def get_step(self):
        return self.New_step

    def set_feedback(self, feedback):
        self.Feedback = feedback

    def get_feedback(self):
        return self.Feedback