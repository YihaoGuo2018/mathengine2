
from problem.BuildProblem import build_character_list
from problem.CharacterList import CharacterList
from problem.Character import Character
import re


def check_format(text=""):
    return True


def process_text(text=""):
    if check_format(text) is False:
        return

    text_separate = []
    answer = text.replace(" ", "")
    text_separate = re.findall(r'[+]|[-+]?[0-9]+|[a-z]+|[()]|[+-/*//]', answer)
    for i in range(len(text_separate)):
        if i - 1 >= 0 and text_separate[i][0] == "-" and re.search('[-+]?[0-9]+', text_separate[i - 1]):
            text_separate.insert(i, "+")
    out_character_list = build_character_list(text_separate)
    return out_character_list


def get_level_1(text=""):
    if len(text) == 1:
        return str(ord(text))
    else:
        out = ""
        for char in text:
            out += str(ord(char))
        return out

def modify_text(text = ""):
    number = float(text)
    while number > 10:
        number /= 10
    return str(number)

def give_level_1(character_list=CharacterList()):
    content = character_list.get_content()
    for i in range(len(content)):
        character = content[i]
        character.set_level_1(get_level_1(character.get_content()))


def give_level_2(character_list=CharacterList()):
    content = character_list.get_content()
    has_left_parenthesis = False
    number_now = 0
    for i in range(len(content)):
        character = Character()
        character = content[i]
        if (not has_left_parenthesis) and (not character.is_left_parenthesis()):
            character.set_level_2(str(number_now))
            number_now += 1
        elif (not has_left_parenthesis) and  character.is_left_parenthesis():
            has_left_parenthesis = True
            character.set_level_2(str(number_now))
            number_now += 1
        elif has_left_parenthesis and (not character.is_right_parenthesis()):
            tmp_value = str(number_now) + character.get_level_1()
            tmp_value = modify_text(tmp_value)
            character.set_level_2(tmp_value)
        elif has_left_parenthesis and character.is_right_parenthesis():
            has_left_parenthesis = False
            number_now += 1
            character.set_level_2(str(number_now))
            number_now += 1


def give_level_3(character_list=CharacterList()):
    content = character_list.get_content()
    has_left_parenthesis = False
    number_now = 0
    for i in range(len(content)):
        character = content[i]
        if (not has_left_parenthesis) and (not character.is_left_parenthesis()):
            character.set_level_3(str(number_now))
            number_now += 1
        elif (not has_left_parenthesis) and  character.is_left_parenthesis():
            has_left_parenthesis = True
            character.set_level_3(str(number_now))

        elif has_left_parenthesis and (not character.is_right_parenthesis()):
            if i > 0 and i + 1 < len(content):
                character.set_level_3(str(number_now))
        elif has_left_parenthesis and character.is_right_parenthesis():
            has_left_parenthesis = False
            character.set_level_3(str(number_now))
            number_now += 1


def value_level_2(character=Character()):
    return character.get_level_2()


def sort_level_2(character_list=CharacterList()):
    character_list.set_content(sorted(character_list.get_content(), key=value_level_2))

    return character_list


def value_level_3(character=Character()):
    return character.get_level_3()


def sort_level_3(character_list=CharacterList()):
    character_list.set_content(sorted(character_list.get_content(), key=value_level_3))

    return character_list

def see_level_2(character_list=CharacterList()):
    out2 = []
    out1 = []
    out = []
    out4 = []
    content = character_list.get_content()
    for i in range(len(content)):
        character = content[i]
        out1.append(character.get_content())
        out2.append(character.get_level_1())
        out.append(character.get_level_2())
        out4.append(character.get_level_3())
    print(out1)
    print(out2)
    print(out)
    print(out4)

#
# tmp = process_text("12 + (2i + 4) + (10 + 46i)")
# give_level_1(tmp)
# give_level_2(tmp)
# give_level_3(tmp)
# see_level_2(tmp)
# tmp = sort_level_2(tmp)
# print("   ")
# see_level_2(tmp)
#
# tmp = sort_level_3(tmp)
# print("   ")
# see_level_2(tmp)
# print(tmp)