''' Project Euler Investigating a Prime Pattern
Problem 146
The smallest positive integer n for which the numbers 
n2+1, n2+3, n2+7, n2+9, n2+13, and n2+27 are consecutive primes is 10. 
The sum of all such integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million? '''

import Functions
import time
import math
start = time.clock()
global primes
primes = []

def primality_test(num):
	global primes
	
	if num in primes:
		return True
	if num % 2 == 0:
		return False
	if num % 3 == 0:
		return False
	
	for i in range(5, math.ceil(math.sqrt(num)), 2):
		if num % i == 0:
			return False
	
	primes.append(num)
	return True
		
	
	
	
	
sum = 1242490
current = 150000000

while current >= 1000000:
	if primality_test(current**2 +27) == True:
		if primality_test(current**2 +13) == True:
			if primality_test(current**2 +9) == True:
				if primality_test(current**2 +7) == True:
					if primality_test(current**2 +3) == True:
						if primality_test(current**2 +1) == True:
							sum += current
	
	current -= 1
	if current % 10000 == 0:
		print('Current number under test is: ',current)

print('Sum of all such numbers under 150e6 is, ',sum)
Functions.runtime(start)