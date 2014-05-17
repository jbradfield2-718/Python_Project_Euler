#---------------------------------------------------------------------------------------------------------
#	Passed an integer, returns a list with digits in that integer
#---------------------------------------------------------------------------------------------------------
import time
import csv
import sys

def decompose_digit(num):
	ls = []
	remain = num
	temp = num
	magnitude = 10
	while( remain > 0 ):
	    temp = remain % magnitude
	    ls.append( round(temp / (magnitude/10) ) )		# We round to the nearest int to prevent floats near the exact
	    remain -= temp
	    magnitude *= 10 					# Increases by an order of magnitude
		
	return ls[::-1]                                         # Reverses the list
	
def str_to_int(str):
    num = 0
    for i in range(0, len(str)):
        if i != (len(str) -1):
            num +=  (ord(str[i]) - 48)*(10**(len(str) - i -1))
        else:
            num += ((ord(str[i]) - 48))
    return num

def import_csv(file):
	ls = []
	with open(file, 'rt') as f:
		reader = csv.reader(f)
		for row in reader:
			ls.append(row)
	return ls[0]

def write_csv(file, ls):

	if sys.version_info >= (3,0,0):
		f = open(file, 'w', newline='')
	else:
		f = open(file, 'wb')
	writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_ALL)
	writer.writerow(ls)
	
def int_to_str(integer, magnitude=10):
	num = ''
	current = 0
	last = -1
	current_mag = magnitude
	
	while (integer % current_mag) != integer:
		last = current
		current = (integer % current_mag) - last
		current = int(current / (current_mag/magnitude))
		num += ( chr( current + 48 ))
		current_mag *= int(magnitude)
	last = current
	current = (integer % current_mag) - last
	current = int(current / (current_mag/magnitude))
	num += ( chr( current + 48 ))
	num = num[::-1]            # Reverses the string

	return num
#=====================================================================================================
# Outputs total runtime from 'start' variable
#=====================================================================================================

def runtime(start):
	runtime=time.clock()-start
	print("The total program runtime was ",runtime," seconds.")
	
#=====================================================================================================
# Builds a list of ASCII characters when passed a string
#=====================================================================================================
def decompose_string(string):
  ls=[]
  for i in range(0, len(string)):
    ls.append(string[i])
  return ls
#====================================================================================================
# Sieve of Eratosthenes algorithm to return prime numbers up to numerical limit
#==================================================================================================== 
def primes_sieve(limit):
	primes_ls = []
	a = []
	for i in range(limit + 1):                  # Initialize the primality list
		a.append(True)
	a[0] = a[1] = False

	multiplier = 2
	factor = 0
	for i in range(len(a)):
		if a[i] == True:
			factor = i*multiplier
			while factor <= limit:
				if factor <= limit:
					a[factor] = False
				multiplier += 1					# Increments multiplier for next pass
				factor = i*multiplier
			multiplier = 2
	
	for i in range(len(a)):
		if a[i] == True:
			primes_ls.append(i)
	return primes_ls
	
#====================================================================================================
# Rotate string by specified number of chars.  Default =1
#====================================================================================================
def rotate(str, rot_num_chars =1):
	if rot_num_chars > len(str):
		return 'Error!'
	
	temp1 = str[0:rot_num_chars]
	temp2 = str[rot_num_chars:]
	
	return temp2 + temp1