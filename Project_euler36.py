''' Project Euler Double-base palindromes
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.) '''

import Functions
import time

start = time.clock()

sum = 0

for i in range(1, 1000000):
	test = i
	if (test % 10) != 0:
		test = Functions.int_to_str(test)
		if test == test[::-1]:
			test = i
			test = Functions.int_to_str(test,2)
			if test[-1] != '0':
				if test == test[::-1]:
					sum += i
					#print('Current sum is ',sum)

print('\nThe final sum of all palindromic numbers is ',sum)
Functions.runtime(start)
'''
def isPalindrome(test):
    return (test == test[::-1])


totalSum = 0
for num in range(0, 1000000):
    if (isPalindrome(str(num))):
        if (isPalindrome(str(bin(num))[2:])):
            totalSum += num

print ("Sum is %d" % totalSum)	
Functions.runtime(start)		
'''			