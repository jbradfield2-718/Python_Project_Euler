''' Project Euler
Consecutive prime sum
Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes? '''

# This program uses brute force solution, and loads a csv of all primes < 1e6.
# Answer in approx 16s.  Not best solution.

import Functions
import time
global primes_ls
primes_ls = Functions.import_csv('primes_1e6.csv')
primes_ls = list(map(int, primes_ls))                       # Need to add list on outside, Python 3

def sum_of_primes(num_terms, start):
	global primes_ls
	ans = primes_ls[start]
	
	for i in range(1, num_terms):
		ans += primes_ls[i]
	
	return ans

start_time = time.clock()

prime_sum = 0
start_index = primes_ls.index(953)
best = 953
best_ls = []
test_sum = 0
ls_of_primes = []


for i in range(start_index, len(primes_ls)):
	index = 3                                       # Incremented start prime unit correct answer.  Must be low prime.
	ls_of_primes = []
	current_prime = primes_ls[i]

	while test_sum < current_prime:
		test_sum += primes_ls[index]
		ls_of_primes.append(primes_ls[index])
		if test_sum == current_prime:
			break
		index += 1

	if test_sum == current_prime:
		best = current_prime
		best_ls = ls_of_primes
		test_sum = 0
		continue

	test_sum = 0

print('The number is, ', best)
print(best_ls)
print(len(best_ls))
Functions.runtime(start_time)