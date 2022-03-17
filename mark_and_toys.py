#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Write your code here
    
    prices.sort()
    print (prices)
    list_of_possible_buy=[]
    
    i=0
    toys_cost=0
    
    while k >= toys_cost:
        
        list_of_possible_buy.append(prices[i])
        toys_cost=sum(list_of_possible_buy)
        i+=1

    list_of_possible_buy.remove(prices[i-1])
    
    print(list_of_possible_buy, 'sum:', sum(list_of_possible_buy))
    
    max_number_of_toys=len(list_of_possible_buy)
    return max_number_of_toys 
  
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
