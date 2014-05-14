''' Project Euler Circular primes
Problem 35
The number, 197, is called a circular prime because all rotations of the digits: 
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million? '''


import Functions
import time

start = time.clock()

circular_ls = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
primes_ls = Functions.primes_sieve(999999)
num = ''

for prime in primes_ls:
	if prime > 97:
		num = Functions.int_to_str(prime)				# num is now a char string corresponding to the integer
		num_rot = len(num) -1
		
		while(num_rot > 0):
			num = Functions.rotate(num)
			if Functions.str_to_int(num) not in primes_ls:
				break
			num_rot -=1
		
		if num_rot == 0:
			circular_ls.append(prime)						# if num_rot drops to zero, passed test, append to circular list	

print('The number of circular primes < 1e6 is ',len(circular_ls))
Functions.runtime(start)

