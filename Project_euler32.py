'''Pandigital products
Problem 32
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is
1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.'''

# Brute force solution.  Answer in approx 10s.  Better algorithm would be to determine bounds of pandigital.

from Functions import decompose_digit,  runtime
import time

def is_pandigital(ls):
    if len(ls) != 9:
        return False
    if 1 in ls and 2 in ls and 3 in ls and 4 in ls and 5 in ls and 6 in ls and 7 in ls and 8 in ls and 9 in ls:
        return True
    return False

def build_digits(num1, num2, prod):
    num1 = str(num1)
    num2 = str(num2)
    prod = str(prod)
    digits = num1 + num2 + prod
    digits = list(digits)
    for i in range(len(digits)):
        digits[i] = int(digits[i])
    return digits

	
start = time.clock()	
digits = []
ls_of_products = []
sum_of_products = 0

for i in range(2, 100):
    for j in range(2, 10000):

        test_prod = i*j

        if test_prod in ls_of_products:
            continue

        test_list = build_digits(test_prod, i, j)

        if is_pandigital(test_list):
            sum_of_products += test_prod
            ls_of_products.append(test_prod)

    if i % 100 == 0:
        print('Current i is: ', i)

print('The sum of products is ', sum_of_products)
runtime(start)
