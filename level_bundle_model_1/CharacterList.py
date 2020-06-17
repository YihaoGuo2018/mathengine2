
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

    def __str__(self):
        out = ""
        for character in self.Content:
            out += character.get_content()
        return out

    def get_content(self):
        return self.Content
