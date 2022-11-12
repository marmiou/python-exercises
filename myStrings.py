def count_string_length(string):
    return len(string)


def count_number_of_chars(string, character):
    return string.count(character)


def count_number_of_digits(string):
    return sum(character.isdigit() for character in string)


def count_number_of_digit_occurence(string, occurence):
    return sum((character == occurence and character.isdigit()) for character in string)


def count_number_of_characters_without_spaces(string):
    space_characters = sum(character.isspace() for character in string)
    return len(string) - space_characters


def count_others(s):
    numbers = sum(c.isdigit() for c in s)
    letters = sum(c.isalpha() for c in s)
    spaces = sum(c.isspace() for c in s)
    others = len(s) - numbers - letters - spaces
    return others


# todo
def find_string_equal_to_reverse(string):
    if string == reversed(string):
        print(string)
    else:
        print("String is not reversed")


def chars_mix_up(a, b):
    # abc + xyz ---> xyc + abz
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]

    return new_a + ' ' + new_b


def winner(erica, bob):
    scoring_table = {"E": 1, "M": 3, "H": 5}
    erica_score, bob_score = 0, 0
    for character in erica:
        erica_score += scoring_table.get(character)
    for character in bob:
        bob_score += scoring_table.get(character)

    if erica_score > bob_score:
        return "Erica"
    elif bob_score > erica_score:
        return "Bob"
    else:
        return


# convert all the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence.
# Use map() function
# def get_lower_and_upper(string):
#     return string.lower(), string.upper()
#
#
# def convert_and_eliminate(string):
#     return set(map(get_lower_and_upper(string), string))
#


if __name__ == '__main__':
    # name_str = "Markella rocks 77111"
    # reversed_string = "alla"
    # chars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
    #
    # print(count_string_length(name_str))
    # print(count_number_of_chars(name_str, "a"))
    # print(count_number_of_digits(name_str))
    # print(count_number_of_digit_occurence(name_str, "1"))
    # print(count_number_of_characters_without_spaces(name_str))
    # print(find_string_equal_to_reverse(reversed_string))
    erica = "EHH"
    bob = "EME"
