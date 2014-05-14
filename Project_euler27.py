''' Project Euler Quadratic primes
Problem 27
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. 
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 
41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values 
n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number 
of primes for consecutive values of n, starting with n = 0. '''

import Functions
import time

def quad_function(n, a, b):
	return n**2 + a*n + b
	
start = time.clock()
primes = Functions.primes_sieve(1002000)
prime_test_ls = Functions.primes_sieve(1000)


n = 0

current_max = 0
current_test = 0
best_a = 0
best_b = 0

for a in range(-999, 1000):
	for b in prime_test_ls:
		while(True):
			if quad_function(n, a, b) in primes:
				current_test += 1
				n += 1
			else:
				n = 0
				break
			
		if current_test > current_max:
			current_max = current_test
			best_a = a
			best_b = b
			print('Current max consecutive primes ',current_max,' Current best a ',best_a,' Current best b ',best_b)
		current_test = 0


print('The product of the coefficients is ',best_a * best_b)
print(quad_function(4,1,41))
Functions.runtime(start)
		