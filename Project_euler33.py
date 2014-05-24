'''Digit canceling fractions
Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, 
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.'''
# Finds answer, 29ms

import time
from Functions import runtime

start_time = time.clock()
ls = []
frac_ls = []
for numerator in range(11, 100):
	for denominator in range(11, 100):
	
		if numerator % 10 == 0:
			continue
		if denominator % 10 == 0:
			continue
		if numerator == denominator:
			continue
			
		value = numerator / denominator
		
		num = str(numerator)
		denom = str(denominator)
		num = list(num)
		denom = list(denom)
		
		#print(num, denom)
		
		for digit in num:
			if digit in denom:
				num.remove(digit)
				denom.remove(digit)
				num = int(num[0])
				denom = int(denom[0])
			
				test = num/denom
			
				if test == value and (numerator / denominator) < 1:
					ls.append(test)
					#frac_ls.append( (numerator,denominator))
				
print(len(ls))
print(ls)
product = 1
for i in ls:
	product *= i
	
print('The value of the denominator is ', 1/product)
runtime(start_time)
