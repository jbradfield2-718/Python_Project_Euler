''' Project Euler
Consecutive prime sum
Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes? '''

import Functions
import time
global primes_ls
primes_ls = Functions.primes_sieve(999999)

def sum_of_primes(num_terms, start):
	global primes_ls
	ans = primes_ls[start]
	
	for i in range(1, num_terms):
		ans += primes_ls[i]
	
	return ans

start = time.clock()
best = 21
prime_sum = 0
limit = 100

for i in range(len(primes_ls)):
	print(primes_ls[i])
	prime_sum = sum_of_primes(best,i)
	if prime_sum in primes_ls:
		current = best -1
		while current <= limit:
			prime_sum += primes_ls[current]
			current += 1
			if current +1 > best:
				best = current +1
				print('current best...',prime_sum)

print('The prime < 1e6 sum of most consecutive primes is ',primes_ls[best -1])
Functions.runtime(start)