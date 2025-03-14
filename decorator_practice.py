from functools import wraps
import random


# Создаем декоратор printing, который печатает результат функции
def printing(func):
    """Декоратор: печатает результат выполнения функции"""

    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) is list:
            for r in result:
                print(f"result = {r}")
        else:
            print(f"result = {result}")
        return result

    return inner


def int_decorator(func):
    """Декоратор преобразования в целочисленное значение (int)"""

    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        result_int = int(result)
        print(f" integer result is {result_int}")
        return result_int

    return inner


@printing
def add_one(x):
    """Добавляет единицу к заданному числу"""
    return x + 1


@printing
def even_numbers(numbers_list: list):
    """Выбирает из списка только четные цифры"""
    even_list = []
    for numb in numbers_list:
        if numb % 2 == 0:
            even_list.append(numb)
    return even_list


@int_decorator
def get_random_number():
    return random.randint(1, 100) / random.randint(1, 100)


if __name__ == "__main__":
    new_number = add_one(12)
    print(new_number)
    users_list = even_numbers([23, 65, 44, 20, 15, 10])
    print(users_list)
    random_number = get_random_number()
    print(random_number)
