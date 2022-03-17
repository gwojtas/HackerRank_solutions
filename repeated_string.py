#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    
        lenght_of_string = len(s)
        strings_in_infinite_string = n//lenght_of_string
        rest_of_string = n % lenght_of_string
        a_in_starting_string=s.count('a')
        rest_of_string_letters=s[0:rest_of_string]
        a_in_rest=s[0:rest_of_string].count('a')
        
        print('lenght of starting strings: ', lenght_of_string)
        print('n_letters:',n)
        print('full strings in first n_letters', strings_in_infinite_string)
        print('rest: ', rest_of_string)
        print('rest of string_letters: ',rest_of_string_letters)
        print('a in starting string', a_in_starting_string)
        print('a in rest: ',a_in_starting_string)
        
        frequency_of_a= (s.count('a') * strings_in_infinite_string)+rest_of_string_letters.count('a')
        print('frequency_of_a', frequency_of_a)
        return frequency_of_a
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
