import random

def generate_arr_same_numbers(number:int, n:int) -> list[int]:
    arr:list[int] = []

    for i in range(n):
        arr.append(number)

    return arr


def generate_arr_reverse_sorted(n: int) -> list[int]:
    arr:list[int] = []

    for i in range(n):
        number: int = random.randint(0, 2)
        arr.append(number)

    arr.sort(reverse=True)
    return arr


def generate_arr_sorted(n: int) -> list[int]:
    arr:list[int] =  generate_arr_reverse_sorted(n)
    arr.sort()
    return arr


def generate_arr_random(n: int) -> list[int]:
    arr:list[int] = []

    for i in range(n):
        number: int = random.randint(0, 2)
        arr.append(number)

    random.shuffle(arr)
    return arr
