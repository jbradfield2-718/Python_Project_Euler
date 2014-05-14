''' Project Euler How many reversible numbers are there below one-billion?
Problem 145
Some positive integers n have the property that the sum [ n + reverse(n) ] 
consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. 
We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. 
Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (109)? '''
import Functions
import time
import string

start = time.clock()

def reverse(num):
	num = str(num)
	num = num[::-1]
	num = Functions.str_to_int(num)
	return num
	
def is_reversible(num):
	print(num)
	num = str(num)
	print(num)
	for i in len(num):
		if int(i) % 2 == 0:
			return False
			
	return True
	
		


sum_reversible = 0
for i in range(1,1000000001):
	test = int(i) + int(reverse(i))
	
	if is_reversible(int(test)) == True:
		sum_reversible += 1

print('The number of reversible numbers < 1e9 is ',sum_reversible)
Functions.runtime(start)
	
	
	