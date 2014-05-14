''' Project Euler Problem 23
    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
    the smallest number that can be written as the sum of two abundant numbers is 24.
    By mathematical analysis, it can be shown that all integers greater than 28123
    can be written as the sum of two abundant numbers. However, this upper limit cannot
    be reduced any further by analysis even though it is known that the greatest number
    that cannot be expressed as the sum of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers. '''

import math
import time
import Functions
from itertools import product

def is_abundant(num):
    test = math.ceil(num/2)
    sum = 0
    while(test > 0):
        if (num % test == 0):
            sum += test
        test -= 1

    if sum > num:
        return True

    return False

start = time.clock()
abundant_ls = []
finalsum = 0

for i in range(0, 28123):
    if (is_abundant(i) == True):
        abundant_ls.append(i)
    if (i % 10000) == 0:
        print('Current num in abundant list ',i)
#print(abundant_ls)

print('Length of list of abundant numbers is ',len(abundant_ls))

a = set(sum(pair) for pair in product(abundant_ls, repeat = 2))

num = 1

while (num < 28124):
	if(num not in a):
		finalsum += num
	num += 1
print(finalsum)
print(Functions.runtime(start))
