"""
Write a Python program to get the Fibonacci series between 0 and 50.
"""

import time

def main():
    j0 = 0
    j1 = 1

    print(j0, end=", ")
    print(j1, end=", ")

    while j0+j1 < 51:
        print(j0 + j1, end=", ")

        jtemp = j0 + j1
        j0 = j1
        j1 = jtemp


if __name__ == "__main__":

    start_time = time.perf_counter()

    main()

    stop_time = time.perf_counter()

    exec_time = stop_time - start_time

    print()
    print(f"The program took {exec_time} sec to run.")
