#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mask = []
    for num in my_list:
        if num % 2 == 0:
            mask.append(True)
        else:
            mask.append(False)
    return mask
