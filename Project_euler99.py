''' Project Euler Largest exponential
Problem 99
Comparing two numbers written in index form like 211 and 37 is not difficult, 
as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, 
as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines 
with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above. '''
import Functions
import time
import math

start = time.clock()
best_line = 1
current_line = 1
best_num = 0
ls = Functions.import_csv('base_exp.txt')

for pair in ls:
	print('Current line under test...',current_line)
	test = int(pair[1]) * math.log(int(pair[0]))		#instead of compare actual base**exp, compare exponent * log(base)
	if test > best_num:
		best_num = test
		best_line = current_line
	current_line += 1

print('The line with the largest number is ', best_line)
Functions.runtime(start)
	