from functools import reduce


def count_list_length(my_list):
    return len(my_list)


def multiply_items_in_list(my_list):
    total = 1
    for item in my_list:
        total *= item
    return total


def get_largest_number(my_list):
    return max(my_list)


def get_min_number(my_list):
    return min(my_list)


# Count the number of strings where the string length is 2 or more and the first and last character are same
# from a given list of strings
def count_items(my_list):
    return len([string for string in my_list if (len(string) > 1 and string[0] == string[-1])])


# Get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def last(n):
    return n[-1]


def sort_list_last(tuples):
    return sorted(tuples, key=last)


# Write a Python program to remove duplicates from a list
def remove_list_duplicates(my_list):
    return list(set(my_list))


def check_is_empty(my_list):
    if len(my_list) == 0:
        return True
    else:
        return False


def clone_list(my_list):
    return my_list.copy()


# Method that takes two lists and returns True if they have at least one common member
def have_common_number(list_a, list_b):
    set_as_list_a = set(list_a)
    if set_as_list_a.intersection(list_b):
        print(list(set_as_list_a.intersection(list_b)))
        return True
    else:
        return False


# Method that gets the difference between the two lists:
def find_difference_of_lists(list_a, list_b):
    return set(list_a).difference(set(list_b))


def access_index_and_value(list_a):
    return [(num_index, num_val) for num_index, num_val in enumerate(list_a)]


# triple all numbers of a given list of integers. Use Python map
def triple_numbers_of_list(list_a):
    return list(map(lambda x: x + x + x, list_a))


# add three given lists using Python map and lambda
def add_lists(list_a, list_b, list_c):
    return list(map(lambda x, y, z: x + y + z, list_a, list_b, list_c))


# MAP EXAMPLE:
def upper_list_with_map(persons):
    return list(map(str.upper, persons))


# FILTER EXAMPLE:
def is_a_student(score):
    return score > 80


def filter_scores(scores):
    return list(filter(is_a_student, scores))


# REDUCE EXAMPLE:
def custom_sum(first, second):
    return first + second


def reduce_numbers(numbers):
    return reduce(custom_sum, numbers)


if __name__ == '__main__':
    sample_list = [1, 2, 3]
    numbs = [10, 20, 30]
    empty_list = []
    list_of_strings = ['abc', 'xyz', 'aba', '1221', 'q', '12345', 'laal']
    list_of_tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    duplicate_list = [1, 1, 2, 3, 4, 5, 6, 7, 7, "cat", "cat", (1, 2), (1, 2)]
    persons_list = ["markella", "leo", "john"]
    score_list = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 92, 85]
    my_numbers = [3, 4, 6, 9, 34, 12]
    print(count_list_length(sample_list))
    print(multiply_items_in_list(sample_list))
    print(get_largest_number(sample_list))
    print(count_items(list_of_strings))
    print(sort_list_last(list_of_tuples))
    print(remove_list_duplicates(duplicate_list))
    print(check_is_empty(sample_list))
    print(clone_list(list_of_strings))
    print(have_common_number(sample_list, duplicate_list))
    print(find_difference_of_lists(sample_list, empty_list))
    print(access_index_and_value(sample_list))
    print(add_lists(sample_list, sample_list, numbs))
    print(upper_list_with_map(persons_list))
    print(filter_scores(score_list))
    print(reduce_numbers(my_numbers))
