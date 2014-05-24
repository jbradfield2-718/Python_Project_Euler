'''Concealed Square
Problem 206
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.'''
# Finds answer.  Very slow.  approx 1200 sec.  Optimize by getting start number closer to desired.

import time
from Functions import runtime

start_time = time.clock()
test = 1000000000

while True:
	num = test ** 2
	
	num = str(num)
	if len(num) > 19:
		print('Code incorrect, missed number!')
		runtime(start_time)
		input()
	
	elif len(num) == 19:
		num = list(num)
		'''print(num)
		for i in range(len(num)):
			print(num[i])
		input()'''
		
		if num[0] == '1' and num[2] == '2' and num[4] == '3' and num[6] == '4' and num[8] == '5' \
		and num[10] == '6' and num[12] == '7' and num[14] == '8' and num[16] == '9' and num[18] == '0':
			break
	test += 1
	if test % 1000000 == 0:
		print('Current num is ', test)
	
print('The desired number is ', test)
runtime(start_time)
		
