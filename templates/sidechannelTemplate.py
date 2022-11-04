import sys
import os
from time import time_ns


# def a function to call a program in the same directory called pin_checker
def call_pin_checker():
    num = "48390510"
    # loop through num and change each digit one at a time
    # ex: 00000000 -> 00000001 -> 00000002 -> 00000003 -> 00000004 -> 00000005 -> 00000006 -> 00000007 -> 00000008 -> 00000009 -> 00000010 -> 00000020 -> 00000030  ...
    # call the pin_checker program
    for i in range(0, 30):
        num = increment_num(num)
        # check how long it takes to run the pin_checker program
        start = time_ns()
        # enter the number
        os.system("echo '" + num + "' | ./pin_checker")
        end = time_ns()

        # write to a file called time.txt the number and the time it took to run the pin_checker program in nanoseconds, formatted num and time
        os.system("echo '" + num + " " + str(end - start) + "' >> time.txt")








# def a function to increment a number
def increment_num(num):
    # increment postition 2 of num by 1 and return num
    if num[7] == "9":
        num = num[0:7] + "0" + num[8:]
        return num
    else:
        num = num[0:7] + str(int(num[7]) + 1) + num[8:]
        return num

if __name__ == "__main__":
    call_pin_checker()
