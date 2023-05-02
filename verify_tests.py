from subprocess import check_output
from datetime import datetime
from generate_tests import *

def is_arr_sorted(arr: list[int]) -> bool:
    ans = False

    if len(arr) == 1:
        return True

    for i in range(len(arr)-1):
        if (arr[i] <= arr[i+1]): ans = True
        else:
            ans = False
            break
    return ans


def verify_option(option: int, counter: int):
    time = 0
    start_time = datetime.now()
    ans = check_output(f"./problem_merge < ./out/option{option}.txt", shell=True)
    time = datetime.now() - start_time
    arr = ans.decode("ascii").split("\n")

    for l in arr:
        if (len(l) > 0):
            arr_item = list(map(int, l.split(" ")))
            print(f"Test #{counter} " + str(is_arr_sorted(arr_item)))
            counter+=1
    
    return time


def start():
    check_output(f"c++ problem_merge.cpp -o problem_merge", shell=True)
    counter = 1

    for i in range(1, 17):
        print(f"Option #{i}")
        print("-------------")
        time = verify_option(i, counter)
        print("Time: " + str(time)[6:len(str(time))])
        counter+=6
        print("-------------")


start()