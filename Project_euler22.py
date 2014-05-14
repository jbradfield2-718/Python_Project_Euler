'''	Project Euler Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file? '''

import csv
import Functions
import time

start = time.clock()
ls = []
sum_names = 0
with open('names.csv', 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        ls.append(row)
ls = ls[0]
ls.sort()

name_string = []
local_sum = 0
for i in range(len(ls)):
	name_string = Functions.decompose_string(ls[i])			# name string now has list of individual chars in name
	for j in range(len(name_string)):
		local_sum += ( ord(name_string[j]) - 64 )
	
	local_sum += (local_sum * i)
	sum_names += local_sum
	local_sum = 0											# resets variable for next pass...

print('The total of all the name scores in the file is ',sum_names)
Functions.runtime(start)

		
