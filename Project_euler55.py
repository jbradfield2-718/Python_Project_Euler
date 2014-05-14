''' Project Euler Problem 52: Lychrel Numbers

    '''

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
		
	return ls[::-1]

def reverse_string(ls):
    return ls[::-1]

def is_lychrel(num):
    ls = []
    ls2 = []

    test = num
    counter = 0

    while(counter < 50):

        ls = decompose_digit(test)
        
        test = 0
        for i in range( 0, len(ls) ):
            test += ls[i] * 10**i

        test += num

        ls = decompose_digit(test)              # Now a string...
        ls2 = reverse_string(ls)

        
        if (ls == ls2):
            return False

        num = test
        counter += 1
        
        
    return True


count_Lychrel = 0
for i in range(0, 10000):
    test = is_lychrel(i)

    if(test == True):
        count_Lychrel += 1

print('The number of Lychrel numbers below 10,000 is ',count_Lychrel)




