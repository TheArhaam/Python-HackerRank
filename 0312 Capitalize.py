#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # name = s.split()

    name = list(s)
    prev = " "
    for i in range(0,len(name)):
        if(name[i].isalpha()):
            if(prev == " "):
                name[i] = name[i].upper()
        prev = name[i]
    res = "".join(name)

    #Cannot be used since string may contain more than one space
    # res = ""
    # for i in range(0,len(name)):
    #     name[i] = list(name[i])
    #     if (name[i][0].isalpha()):
    #         name[i][0] = name[i][0].upper()
    #     name[i] = "".join(name[i])
    #     res = res + name[i] + " "

    #Cannot be used since string may contain any number of words
    # #For first name
    # fname = list(name[0])
    # fname[0] = fname[0].upper()
    # fname = "".join(fname)
    # #For last name
    # lname = list(name[1])
    # lname[0] = lname[0].upper()
    # lname = "".join(lname)
    # res = fname + " " + lname
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
