from typing import List


def find_missing_value_linear_runtime(listed_numbers:List[int], subset_size: int):
    """
    This method aims finding the missing values from the subset
    of natural numbers lower than a number n

    >>> listed_values = [3,1,2,5]
    >>> find_missing_value_linear_runtime(listed_values, len(listed_values)+1)
    [4]
    >>> listed_values = [1,3,2,4,5,7,9,8]
    >>> find_missing_value_linear_runtime(listed_values, 9)
    [6]
    >>> listed_values = [1,3,2,4,5,7,9,8,11]
    >>> find_missing_value_linear_runtime(listed_values, 11)
    [6, 10]
    """
    indexed_list = [int]*subset_size
    for number in listed_numbers:
        indexed_list[number-1] = number  # python list indexes starts at 0
    missing_numbers = []
    for index, indexed_number in enumerate(indexed_list):
        expected_number = index+1
        if indexed_number != expected_number:
            missing_numbers.append(expected_number)  # python list indexes starts at 0
    return missing_numbers
