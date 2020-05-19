 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong

    isdigit_pass = False
    islower_pass = False
    isupper_pass = False  
    issplchar_pass = False 
    validations_pass = 0 
    for char in password:
        if char.isdigit() and not isdigit_pass:
            validations_pass += 1 
            isdigit_pass = True
            #print("digit")
        elif char.isalpha():
            if char.islower() and not islower_pass:
                validations_pass +=1 
                islower_pass = True 
                # print("lower")
            elif char.isupper() and not isupper_pass:
                validations_pass +=1
                isupper_pass = True 
                # print("upper")
        elif not char.isdigit() and not char.isalpha() and not issplchar_pass :
            validations_pass +=1
            issplchar_pass = True 
            # print("spl")
        else:
            pass
    # print(validations_pass)
    if len(password)<6:
        return max(6-len(password), 4-validations_pass)
    else:
        return int(4-validations_pass)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
