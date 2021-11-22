#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#


def fizzBuzz(n):
    lst_n=[]
    # Write your code here  
    for i in range (1,n+1):
        lst_n.append(i)
    get_multiple(lst_n)

def get_multiple(lst):
    message=''
    if isinstance(lst,list):
        for i in lst:
            if (i % 3 ==0) and (i% 5 ==0):
                print ('FizzBuzz')
            elif (i % 3 ==0) and not (i% 5 ==0) :
                print ('Fizz')
            elif not (i % 3 ==0) and  (i% 5 ==0) :
                print ('Buzz')
            elif not (i % 3 ==0) and not (i% 5 ==0):
                print (i)
            # print (message)
    else:
        return 'erreur'

n=int(input())
fizzBuzz(n)
# if __name__ == '__main__':
#     n = int(input().strip())

#     fizzBuzz(n)
