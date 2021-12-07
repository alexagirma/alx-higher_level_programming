#!/usr/bin/python3

"""Write a class Square that defines a square
uing a getter and a setter"""


class Square:

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must de >= 0")
        self.__size = value

    def area(self):
        return(self.__size * self.__size)

    def my_print(self):
        if (self.__size == 0):
            print("")
        for x in range(0, int(self.__size)):
            print("#" * int(self.__size))
