"""
Problem
Given a list of account ID numbers (integers) which contains duplicates,
find the one unique integer. (the list is guaranteed to only have one unique (non-duplicated) integer

Requirements
Do not use built-in Python functions or methods
"""


def find_unique(id_list):
    unique_id = 0

    for i in id_list:
        # print("This is the current id being checked:", i)
        # print("This is the current unique id:", unique_id)
        # print("This is the result of the XOR:", unique_id ^ i)
        unique_id ^= i

    return unique_id


if __name__ == '__main__':
    a = find_unique([1, 2, 3, 4, 3, 2, 1])
    print(a)
