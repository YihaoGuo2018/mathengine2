
class CharacterList:

    def __init__(self):
        self.Content = []
        self.Easy_Look = ""

    def add_character(self, character):
        self.Content.append(character)

    def __eq__(self, other):
        return self.Content == other.Content

    def set_easy_see(self, easy_see):
        self.Easy_Look = easy_see

    def set_content(self, content):
        self.Content = content

    def get_content(self):
        return self.Content

    def __str__(self):
        return self.Easy_Look
