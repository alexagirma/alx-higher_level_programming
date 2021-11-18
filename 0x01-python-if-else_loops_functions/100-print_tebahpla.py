#!/usr/bin/python3
for letter in range(ord('z'), ord('a') - 1, -1):  # ord expects a strin
print("{:c}".format(letter if letter % 2 == 0 else letter - 32), end="")
    #  specify :c ptherwise print numbers
