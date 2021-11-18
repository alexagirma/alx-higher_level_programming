#!/usr/bin/python3
def remove_char_at(str, n):  # n is the position
if n >= 0:
str = str[0:n] + str[n + 1:]  # runs to position and adds 1 to replace
return str
