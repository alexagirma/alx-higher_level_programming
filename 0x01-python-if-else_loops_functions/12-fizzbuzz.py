#!/usr/bin/python3
def fizzbuzz():
for runner in range(1, 101):
if runner % 3 == 0 and runner % 5 == 0:
print("FizzBuzz", end=' ')
elif runner % 3 == 0:
print("Fizz", end=' ')
elif runner % 5 == 0:
print("Buzz", end=' ')
else:
print("{}".format(runner), end=' ')
