#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for nums in my_list[::-1]:  # also reversed works
            print("{:d}".format(nums))
