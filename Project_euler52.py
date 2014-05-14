''' Project Euler Problem 52: Permuted Multiples
    It can be seen that the number, 125874, and its double,
    251748, contain exactly the same digits, but in a different order.

    Find the smallest positive integer, x, such that
    2x, 3x, 4x, 5x, and 6x, contain the same digits. '''

def decompose_digit(num):
	ls = []
	remain = num
	temp = num
	magnitude = 10
	while( remain > 0 ):
	    temp = remain % magnitude
	    ls.append(temp / (magnitude/10) )
	    remain -= temp
	    magnitude *= 10 					# Increases by an order of magnitude
		
	return ls[::-1]                                         # Reverses the list

max = 7
num = 10
multiplier = 2
while (multiplier < max):
    multiplier = 2
    test = num
    match = decompose_digit(num)
    list.sort(match)                         # This is the list to test against
    #print(match)
    
    while ( multiplier < max ):
        test *= multiplier
        test = decompose_digit(test)
        list.sort(test)

               
        if( test == match ):
            multiplier += 1
            test = num
        else:
            multiplier = 2
            break

    if(multiplier == max):
        break
    num += 1                    # Increments test number
    if(num % 10000 == 0):
        print("current number under test is ", num)

print(num)   
