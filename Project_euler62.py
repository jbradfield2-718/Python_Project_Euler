'''Cubic permutations
Problem 62
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053).
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.'''

from itertools import permutations
from Functions import runtime
from decimal import *
import time

def is_cube(num):
	test = Decimal( num ** (1/3.0) )  % 1
	if  test < 0.0000005 or test > 0.99999999:
		return True
	return False

def permute(num):
	num = str(num)
	num = list(num)
	result = set(permutations(num))
	return result

start_time = time.clock()

test_num = 2030000000                        # Already tested above 100000000
start_iter_time = time.clock()
while True:
	if is_cube(test_num):
		test_lst = permute(test_num)
		num_cube = 0

		for item in test_lst:
			if is_cube( int(''.join(map(str,item))) ):
				num_cube += 1

		if num_cube >= 3:
			print('Found number with cubes ', test_num, num_cube)

		if num_cube == 5:
			runtime(start_time)

	test_num += 1
	if test_num % 10000000 == 0:
		print('Current number under test is ', test_num)
		print('Elapsed time since last 10e6 ',time.clock() - start_iter_time)
		start_iter_time = time.clock()
