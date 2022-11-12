from itertools import chain
from operator import itemgetter


# sort (ascending and descending) a dictionary by value
def sort_by_value_desc(my_dict):
    return dict(sorted(my_dict.items(), key=itemgetter(1), reverse=True))


# The key= parameter of sort requires a key function (to be applied to be objects to be sorted) rather than a single
# key value and that is just what operator.itemgetter(1) will give you: A function that grabs the first item from
# a list-like object.
def sort_by_value_asc(my_dict):
    return dict(sorted(my_dict.items(), key=itemgetter(1), reverse=False))


# sort (ascending and descending) a dictionary by key
def sort_by_key_desc(my_dict):
    return dict(sorted(my_dict.items(), key=itemgetter(0), reverse=True))


def sort_by_key_asc(my_dict):
    return dict(sorted(my_dict.items(), key=itemgetter(0), reverse=False))


# merge two Python dictionaries
def merge_dictionaries(dict_a, dict_b):
    copy_of_a = dict_a.copy()
    copy_of_a.update(dict_b)
    return copy_of_a


def sum_items_in_dict(dict_a):
    return sum(dict_a.values())


def multiple_items_in_dict(dict_a):
    mult = 1
    for value in dict_a.values():
        mult *= value
    return mult


def remove_key_from_dict(dict_a, key):
    dict_a.pop(key)
    return dict_a


# map 2 lists in a dictionary as key-value
def map_lists_in_dictionary(list_a, list_b):
    return dict(zip(list_a, list_b))


def get_max_value(dict_a):
    return max(dict_a.values())


def get_min_value(dict_a):
    return min(dict_a.values())


def remove_duplicates(dict_a):
    unique = {}
    # return {key: value for key, value in dict_a.items() if value not in unique.values()}
    for key, value in dict_a.items():
        if value not in unique.values():
            unique[key] = value
    return unique


def check_is_empty(dict_a):
    if len(dict_a.values()) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    sample_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0, 5: 3, 6: 3}
    another_dict = {8: 3, 6: 4, 7: 5}
    sample_list = [1, 2, 3, 4]
    another_list = [1, 2, 3]
    empty_dict = {}
    print(sort_by_key_asc(sample_dict))
    print(sort_by_key_asc(sample_dict))
    print(sort_by_value_asc(sample_dict))
    print(sort_by_value_asc(sample_dict))
    print(merge_dictionaries(sample_dict, another_dict))
    print(sum_items_in_dict(sample_dict))
    print(multiple_items_in_dict(another_dict))
    print(remove_key_from_dict(sample_dict, 0))
    print(map_lists_in_dictionary(sample_list,another_list))
    print(get_max_value(sample_dict))
    print(get_min_value(sample_dict))
    print(remove_duplicates(sample_dict))
    print(check_is_empty(empty_dict))
