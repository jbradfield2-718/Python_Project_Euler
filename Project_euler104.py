'''Pandigital Fibonacci ends
Problem 104
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, 
is the first Fibonacci number for which the last nine digits are 1-9 pandigital 
(contain all the digits 1 to 9, but not necessarily in order). 
And F2749, which contains 575 digits, is the first Fibonacci number for which the 
first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits 
AND the last nine digits are 1-9 pandigital, find k.'''
# Gets correct answer.  VERY slow. > 1hr.

import time
from Functions import fibonacci, is_pandigital, runtime

start_time = time.clock()


start = 256100				#232800						#41300
n_minus1 = 0
n_minus2 = 0

while True:
	if n_minus1 > 0 and n_minus2 > 0:
		test = fibonacci(0,n_minus1, n_minus2)
	else:
		test = fibonacci(start)

	n_minus2 = n_minus1
	n_minus1 = test
	test = str(test)
	#print(test)

	a = list( test[0:9] )
	b = list(test[-9:])
	#print(a,b)

	testa = is_pandigital(a)
	testb = is_pandigital(b)
	#print(testa, testb)
	#input()
	if testa and testb:
		print('here!')
		break

	if testa:
		print('one arg true, arg is front.')
		print(start)
	if testb:
		print('one arg true, arg is end.')
		print(start)

	start += 1
	if start % 100 == 0:
		print('current under test ', start)

print('Fibonacci number desired is ', start)
runtime(start_time)