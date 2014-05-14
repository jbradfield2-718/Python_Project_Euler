''' Project Euler Truncatable primes
Problem 37
The number 3797 has an interesting property. Being prime itself, it is possible to continuously 
remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes. '''

import Functions
import time

start = time.clock()
count = 0
sum = 0

primes_ls = Functions.primes_sieve(1000000)
test_ls = primes_ls[4:]

for prime in test_ls:
	test = str(prime)
	while len(test) > 0:
		test = test[1:]
		if len(test) == 0:
			break
		if int(test) not in primes_ls:
			break
	
	if len(test) == 0:
		test = str(prime)
		while len(test) > 0:
			test = test[0:-1]
			if len(test) == 0:
				break
			if int(test) not in primes_ls:
				break
	
	if len(test) == 0:
		count +=1
		sum += prime
		print('Current count is ',count)
	if count == 11:
		break
		
print('The sum of the primes is ',sum)
Functions.runtime(start)	
		