import re





class Character:

    def __init__(self):
        self.Content = ""
        self.Integer = 0
        self.Positive = 0
        self.Negative = 0
        self.Left_parenthesis = 0  # (
        self.Right_parenthesis = 0  # )
        self.Left_bracket = 0  # [
        self.Right_bracket = 0  # ]
        self.Left_braces = 0  # [
        self.Right_braces = 0  # ]
        self.Plus_symbol = 0  # +
        self.Minus_symbol = 0  # -
        self.Division_symbol = 0  # /
        self.Multiplication_symbol = 0  # *
        self.Equal_symbol = 0  # =
        self.Percent_symbol = 0  # %
        self.Single_letter = 0

        self.Level_1 = "0"
        self.Level_2 = "0"
        self.Level_3 = "0"
    def set_content(self, content=""):
        if type(content) != str:
            print("warning !!!!       Character.content")
            return
        if content == "":
            print("warning !!! the content set to character is empty, so content not change")
            return
        self.Content = content
        if content == "(":
            self.set_left_parenthesis()
        elif content == ")":
            self.set_right_parenthesis()
        elif content == "[":
            self.set_left_bracket()
        elif content == "]":
            self.set_right_bracket()
        elif content == "{":
            self.set_left_braces()
        elif content == "}":
            self.set_right_braces()
        elif content == "+":
            self.set_plus_symbol()
        elif content == "-":
            self.set_minus_symbol()
        elif content == "/":
            self.set_division_symbol()
        elif content == "*":
            self.set_multiplication_symbol()
        elif content == "=":
            self.set_equal_symbol()
        elif content == "%":
            self.set_percent_symbol()
        elif len(content) == 1 and content.isalpha():
            self.set_single_letter()
        elif (content[0] == "+" or content[0] == "-") and content[1:].isdigit():
            self.set_integer()
            if content[0] == "+":
                self.set_positive()
            else:
                self.set_negative()
        elif content.isdigit():
            self.set_integer()
            self.set_positive()
        else:
            print("warning !!! the content \"" + content + "\"set to character is not normal")



    def set_level_1(self, value):
        self.Level_1 = value

    def get_level_1(self):
        return self.Level_1

    def set_level_2(self, value):
        self.Level_2 = value

    def get_level_2(self):
        return self.Level_2

    def set_level_3(self, value):
        self.Level_3 = value

    def get_level_3(self):
        return self.Level_3

    def refresh_feature(self):
        self.Integer =  0
        self.Positive = 0
        self.Negative = 0
        self.Left_parenthesis = 0  # (
        self.Right_parenthesis = 0  # )
        self.Left_bracket = 0  # [
        self.Right_bracket = 0  # ]
        self.Left_braces = 0  # [
        self.Right_braces = 0  # ]
        self.Plus_symbol = 0  # +
        self.Minus_symbol = 0  # -
        self.Division_symbol = 0  # /
        self.Multiplication_symbol = 0  # *
        self.Equal_symbol = 0  # =
        self.Percent_symbol = 0  # %
        self.Single_letter = 0

    def set_left_parenthesis(self):
        self.refresh_feature()
        self.Left_parenthesis = 1

    def is_left_parenthesis(self):
        return self.Left_parenthesis

    def set_right_parenthesis(self):
        self.refresh_feature()
        self.Right_parenthesis = 1

    def is_right_parenthesis(self):
        return self.Right_parenthesis

    def set_left_bracket(self):
        self.refresh_feature()
        self.Left_bracket = 1

    def is_left_bracket(self):
        return self.Left_bracket

    def set_right_bracket(self):
        self.refresh_feature()
        self.Right_bracket = 1

    def is_right_bracket(self):
        return self.Right_bracket

    def set_left_braces(self):
        self.refresh_feature()
        self.Left_braces = 1

    def is_left_braces(self):
        return self.Left_braces

    def set_right_braces(self):
        self.refresh_feature()
        self.Right_braces = 1

    def is_right_braces(self):
        return self.Right_braces

    def set_integer(self):
        self.refresh_feature()
        self.Integer = 1

    def is_integer(self):
        return self.Integer

    def set_positive(self):
        self.Positive = 1
        self.Negative = 0

    def is_positive(self):
        return self.Positive

    def set_negative(self):
        self.Positive = 0
        self.Negative = 1

    def is_negative(self):
        return self.Negative

    def set_plus_symbol(self):
        self.refresh_feature()
        self.Plus_symbol = 1

    def is_plus_symbol(self):
        return self.Plus_symbol

    def set_minus_symbol(self):
        self.refresh_feature()
        self.Minus_symbol = 1

    def is_minus_symbol(self):
        return self.Minus_symbol

    def set_division_symbol(self):
        self.refresh_feature()
        self.Division_symbol = 1

    def is_division_symbol(self):
        return self.Division_symbol

    def set_multiplication_symbol(self):
        self.refresh_feature()
        self.Multiplication_symbol = 1

    def is_multiplication_symbol(self):
        return self.Multiplication_symbol

    def set_equal_symbol(self):
        self.refresh_feature()
        self.Equal_symbol = 1

    def is_equal_symbol(self):
        return self.Equal_symbol

    def set_percent_symbol(self):
        self.refresh_feature()
        self.Percent_symbol = 1

    def is_percent_symbol(self):
        return self.Percent_symbol

    def set_single_letter(self):
        self.refresh_feature()
        self.Single_letter = 1

    def is_single_letter(self):
        return self.Single_letter

    def __eq__(self, other):
        return self.Content == other.Content

    def get_content(self):
        return self.Content
