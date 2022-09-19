"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return list(map(lambda num: num ** 2, numbers))


def is_prime(num):
    """
    функция, которая проверяет является ли число простым
    :param num: только натуральные числа
    :return: bool
    """
    '''
    less optimal
    if len([i for i in range(1, num+1) if num % i == 0]) == 2:
        return True
    else:
        return False
    '''
    if num == 0 or num == 1:
        return False
    else:
        a = True
        for i in range(2, num):
            if num % i == 0:
                a = False
                break
        return a


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(lambda num: num % 2 != 0, numbers))
    elif filter_type == EVEN:
        return list(filter(lambda num: num % 2 == 0, numbers))
    elif filter_type == PRIME:
        return list(filter(is_prime, numbers))