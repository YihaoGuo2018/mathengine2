import re
from level_bundle_model_1.BaseFeature import BaseFeature

class Character:

    def __init__(self):
        self.Content = ""
        self.Base_Feature = BaseFeature()

    def set_content(self, content=""):
        if type(content) != str:
            print("warning !!!!       Character.content")
            return
        if content == "":
            print("warning !!! the content set to character is empty, so content not change")
            return
        self.Content = content

        if content == "(":
            self.Base_Feature.set_left_parenthesis()
        elif content == ")":
            self.Base_Feature.set_right_parenthesis()
        elif content == "[":
            self.Base_Feature.set_left_bracket()
        elif content == "]":
            self.Base_Feature.set_right_bracket()
        elif content == "{":
            self.Base_Feature.set_left_braces()
        elif content == "}":
            self.Base_Feature.set_right_braces()
        elif content == "+":
            self.Base_Feature.set_plus_symbol()
        elif content == "-":
            self.Base_Feature.set_minus_symbol()
        elif content == "/":
            self.Base_Feature.set_division_symbol()
        elif content == "*":
            self.Base_Feature.set_multiplication_symbol()
        elif content == "=":
            self.Base_Feature.set_equal_symbol()
        elif content == "%":
            self.Base_Feature.set_percent_symbol()
        elif len(content) == 1 and content.isalpha():
            self.Base_Feature.set_single_letter()
        elif (content[0] == "+" or content[0] == "-") and content[1:].isdigit():
            self.Base_Feature.set_integer()
            if content[0] == "+":
                self.Base_Feature.set_positive()
            else:
                self.Base_Feature.set_negative()
        elif content.isdigit():
            self.Base_Feature.set_integer()
            self.Base_Feature.set_positive()
        else:
            print("warning !!! the content \"" + content + "\"set to character is not normal")

    def refresh_feature(self):
        self.Base_Feature.refresh_feature()

    def is_left_parenthesis(self):
        return self.is_left_parenthesis()

    def is_right_parenthesis(self):
        return self.is_right_parenthesis()

    def is_left_bracket(self):
        return self.is_left_bracket()

    def is_right_bracket(self):
        return self.is_right_bracket()

    def is_left_braces(self):
        return self.is_left_braces()

    def is_right_braces(self):
        return self.is_right_braces()

    def is_integer(self):
        return self.is_integer()

    def is_positive(self):
        return self.is_positive()

    def is_negative(self):
        return self.is_negative()

    def is_plus_symbol(self):
        return self.is_plus_symbol()

    def is_minus_symbol(self):
        return self.is_minus_symbol()

    def is_division_symbol(self):
        return self.is_division_symbol()

    def is_multiplication_symbol(self):
        return self.is_multiplication_symbol()

    def is_equal_symbol(self):
        return self.is_equal_symbol()

    def is_percent_symbol(self):
        return self.is_percent_symbol()

    def is_single_letter(self):
        return self.is_single_letter()

    def __eq__(self, other):
        return self.Content == other.Content

    def get_content(self):
        return self.Content
