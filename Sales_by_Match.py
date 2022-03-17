#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    
 
    sorting_socks=[]
    number_of_pairs=0
    
    for i in list(set(ar)):
        sorting_socks.append(ar.count(i))
     
    for x in sorting_socks:
        if x>=2:
            number_of_pairs += x//2
  
    return number_of_pairs
    
    
   ## for i in range(n):
      #  current_sock =ar[n]
        
       # for m in range(min(i+1,n-1),n):
            
          #  if current_sock == m:
            #    number_of_socks_matching_in_color+=1
              #  print(number_of_socks_matching_in_color)
            
            
        
        
    
 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()