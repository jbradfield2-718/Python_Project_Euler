''' Project Euler: Number spiral diagonals
Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way? '''

import time
import Functions
import numpy

def update_pos(shift, change_shift, row, column):
	
	if shift == 1:
		return (shift +1, row, column -1)
	
	elif shift == 2:
		return (shift +1, row-1, column)
	
	elif shift == 3:
		return (shift +1, row, column +1)
	
	elif shift == 4:
		return (1, row +1, column)
		
	else:
		return 'Error'


	

shift = 1			# 1=right 2=down 3=left 4=up
change_shift = 1	# Reset at 2
move_cnt = 0
max_move = 1		# 
num = 2
row = 500
column = 500 

num_arr = numpy.zeros((1001,1001))
num_arr[500][500] = 1


while row < 1001 and row > 0 and column < 1001 and column > 0:
	(shift,row,column) = update_pos(shift, row, column)
	print(row,column)
	num_arr[row][column] = num
	num += 1


print(num_arr)