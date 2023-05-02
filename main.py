from generate_tests import *
from files import write_file
import random

cotas = [1, 10, 100, 200, 300]

def generate_option_1():
    for k in range(1, 5):
        content: str = ""
        for i in range(6):
            number: int = random.randint(0, 2)
            n: int = random.randint(cotas[k-1], cotas[k])
            ans:list[int] = generate_arr_same_numbers(number, n)
            content += f"{n}\n" + str(ans).replace(',', '').replace('[', '').replace(']', '') + "\n"
        write_file(f"./out/option{k}", content)


def generate_option_2():
    for k in range(1, 5):
        content: str = ""
        for i in range(6):
            n: int = random.randint(cotas[k-1], cotas[k])
            ans:list[int] = generate_arr_reverse_sorted(n)
            content += f"{n}\n" + str(ans).replace(',', '').replace('[', '').replace(']', '') + "\n"
        write_file(f"./out/option{k+4}", content)


def generate_option_3():
    for k in range(1, 5):
        content: str = ""
        for i in range(6):
            n: int = random.randint(cotas[k-1], cotas[k])
            ans:list[int] = generate_arr_random(n)
            content += f"{n}\n" + str(ans).replace(',', '').replace('[', '').replace(']', '') + "\n"
        write_file(f"./out/option{k+8}", content)


def generate_option_4():
    for k in range(1, 5):
        content: str = ""
        for i in range(6):
            n: int = random.randint(cotas[k-1], cotas[k])
            ans:list[int] = generate_arr_sorted(n)
            content += f"{n}\n" + str(ans).replace(',', '').replace('[', '').replace(']', '') + "\n"
        write_file(f"./out/option{k+12}", content)


def main():
    generate_option_1()
    generate_option_2()
    generate_option_3()
    generate_option_4()


main()
