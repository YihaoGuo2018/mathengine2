

class State:
    def __init__(self):

        self.Step = 0
        # self.Finish = 0
        # self.Step_Limit = 0

    def add_step(self):
        self.Step += 1

    def get_step(self):
        return self.Step

    def set_step(self, step):
        self.Step = step
