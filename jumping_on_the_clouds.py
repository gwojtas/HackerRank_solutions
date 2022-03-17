#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    
    min_jumps=0
    i=0
    jumps=0
    while i < (len(c)-3):
        if c[i+2]==0:
            jumps+=1
            i+=2
        else:
            jumps+=1
            i+=1
        print(i, jumps)    
            
    min_jumps=jumps+1
    return min_jumps
    
    
 
    
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
