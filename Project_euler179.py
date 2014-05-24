'''Consecutive positive divisors
Problem 179
Find the number of integers 1 < n < 107, for which n and n + 1 have the same number of positive divisors.
For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.'''
# VEEEEEEEEEEEERY SLOW.  Over 1hr, but gets correct solution.

from Functions import runtime, import_csv
import time, functools
global primes_ls

def factors(n):
	facts = set(functools.reduce(list.__add__,
				([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
	return len(facts)


start_time = time.clock()
primes_ls = import_csv('primes_1e7.csv')
primes_ls = primes_ls[0]
for prime in primes_ls:
	prime = int(prime)

sum = 0
last_div = factors(10000001)
for num in range(10000000, 1, -1):
	current = factors(num)
	if last_div == current:
		sum +=1
	last_div = current
	if num % 1000000 == 0:
		print('Current number under test is ', num)

print('desired num is ', sum)
runtime(start_time)
