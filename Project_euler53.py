'''Combinatoric selections
Problem 53
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =
n!
r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?'''

# This works, answer in 19ms

from math import factorial
from Functions import runtime
import time

def combinations(num, choose):
    numerator = factorial(num)
    denominator = factorial(choose) * factorial(num - choose)

    return numerator/denominator

start_time = time.clock()
num_of_combinations = 0
for num in range(23, 101):
    for choose in range(num, 0, -1):
        if combinations(num, choose) > 1000000:
            num_of_combinations += 1

print('The number of combinations > 1e6 is ', num_of_combinations)
runtime(start_time)
