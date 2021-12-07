#!/usr/bin/python3
"""
Defines class Square
"""


class Square:
    """ defines private attribute """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """ defines repr """
    def __repr__(self):
        return self.my_print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or all(value) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    """ prints square with # in stdout """
    def my_print(self):
        if self.size == 0:
            print()
        else:
            x = self.position[0]
            y = self.position[1]
            for i in range(y):
                print("")
            for row in range(self.size):
                for j in range(x):
                    print(" ", end="")
                for col in range(self.size):
                    print("#", end="")
                print()

    """ returns area of the square """
    def area(self):
        return self.size ** 2

    """ prints square with # """
    def __str__(self):
        square = []
        if self.__size == 0:
            return "\n"
        else:
            x = self.position[0]
            y = self.position[1]
            for i in range(y):
                square.append("\n")
            for row in range(self.size):
                for j in range(x):
                    square.append(" ")
                for col in range(self.size):
                    square.append("#")
                if row < self.__size - 1:
                    square.append("\n")
        square = "".join(square)
        return square
