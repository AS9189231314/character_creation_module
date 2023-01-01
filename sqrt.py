"""Calculate the square root of a number."""
from math import sqrt
from typing import Any

message: str = 'Добро пожаловать в самую лучшую программу \n'\
               ' для вычисления квадратного корня из заданного числа '


def calculate_square_root(number: Any) -> float:
    """Calculate the square root of a number."""
    return sqrt(number)


def calc(number: float) -> Any:
    """Take a number and returns the square root of that number."""
    if number <= 0:
        print('Не возможно вычислить квадратный корень из введенного числа.')
    else:
        num = calculate_square_root(number)
        print(f'Мы вычислили квадратный корень из введённого вами числа.\n'
              f' Это будет: {num}')


print(message)
calc(25.5)
