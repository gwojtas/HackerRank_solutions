import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    

    next_step=0
    course=[0]
    number_of_valley=0
    
    for step in path:
        if step =='D':
            next_step-=1
            course.append(next_step)
            
        if step =='U':
            next_step+=1 
            course.append(next_step)  
        
    for high in range(0, len(course)):
            
        if course[high] ==0 and course[high-1]==-1:
            number_of_valley+=1
                
        
    print('Course of the path: ',course)
    print('number of valley: ',number_of_valley)
    return number_of_valley 
    
    
    
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
