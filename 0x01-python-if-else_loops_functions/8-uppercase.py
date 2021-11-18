#!/usr/bin/python3
def uppercase(str):
for reader in range(len(str)):
upper = ord(str[reader])
if upper >= 97 and upper <= 122:
upper = upper - 32
uppertochar = chr(upper)
print("{}".format(uppertochar), end="")
print()
