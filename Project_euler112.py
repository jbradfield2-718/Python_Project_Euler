''' Project Euler Bouncy numbers
Problem 112
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand 
(525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of 
bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%. '''

import Functions
import time

start = time.clock()

def bouncy_test(str):
	increasing = 0
	decreasing = 0
	last = str[0]
	test = str[1]
	inc = 2	
	if test == last:
		while True:
			test = str[inc]
			if test == last:
				inc += 1
				if inc == len(str):
					return False
			else:
				if test > last:
					increasing = 1
					last = test
					inc += 1
					break
				if test < last:
					decreasing = 1
					last = test
					inc +=1
					break
	
	elif test > last:
		increasing = 1
		last = test
	elif test < last:
		decreasing = 1
		last = test
	
				
	#print(decreasing,increasing)	
	for i in range(inc,len(str)):
		test = str[i]
		if decreasing == 1:
			if test > last:
				return True
		if increasing == 1:
			if test < last:
				return True
		#print(last, test)
		last = test
		
		#a = input()
	return False

num = 21781
bouncy = 10890
percent = .9

while True:
	if bouncy_test(str(num)) == True:
		bouncy += 1
		percent = bouncy / num
		if percent >= .99:
			break
	num += 1
	if num % 100000 == 0:
		print('Current number under test is ',num)
		print('Current % of bouncy numbers is ',percent)

print('Number at which bouncy == 99% is ', num)
print('Percent is ',percent)
Functions.runtime(start)

