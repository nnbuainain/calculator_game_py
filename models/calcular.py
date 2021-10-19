from random import randint
from random import choice

op_dict = {'sum': '+', 'subtraction': '-', 'multiplication': '*'}


class Calculator():
    def __init__(self, dif_level: str):
        self.__dif_level = dif_level
        self.__value1 = self.generate_value()
        self.__value2 = self.generate_value()
        self.__operation = choice(list(op_dict))
        self.__result = self.generate_result()

    @property
    def dif_level(self) -> str:
        return self.__dif_level

    @property
    def value1(self) -> int:
        return self.__value1

    @property
    def value2(self) -> int:
        return self.__value2

    @property
    def operation(self):
        return self.__operation

    @property
    def result(self):
        return self.__result

    def generate_value(self) -> str:
        if self.__dif_level.lower() in ['1','easy']:
            return randint(1, 10)
        elif self.__dif_level.lower() in ['2','intermediate']:
            return randint(11, 100)
        elif self.__dif_level.lower() in ['3','hard']:
            return randint(101, 1000)
        elif self.__dif_level.lower() in ['4','expert']:
            return randint(1001, 10000)

    def generate_result(self) -> int:
        if self.__operation == 'sum':
            return (self.__value1 + self.__value2)
        elif self.__operation == 'subtraction':
            return (self.__value1 - self.__value2)
        elif self.__operation == 'multiplication':
            return (self.__value1 * self.__value2)

    def show_operation(self) -> str:
        return f'\nHere is your challenge... you got ' \
               f'{self.__operation.upper()}!! provide the answer to the following operation:\n ' \
               f'{self.__value1} {op_dict.get(self.__operation)} {self.__value2} = ?'


