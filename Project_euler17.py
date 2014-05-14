''' Project Euler Problem 17 '''
def decompose_digit(num):
    ones = num % 10
    remain = num - ones

    tens = (remain % 100)/10
    remain = remain - (tens * 10)

    hundreds = (remain % 1000)/100
    remain = remain - (hundreds * 100)

    if(num > 999):
        thousands = 1
    else:
        thousands = 0

    return (ones, tens, hundreds, thousands)

def get_num_letters(num):
    if(num == 1 or num == 2 or num == 6):
        return 3
    if(num == 4 or num == 5 or num == 9):
        return 4
    if(num == 3 or num == 7 or num == 8):
        return 5

def get_tens_letters(num):
    if (num == 1):
        return 3
    if (num == 4 or num == 5 or num == 6):
        return 5
    if (num == 2 or num == 3 or num == 8 or num == 9):
        return 6
    else:
        return 7

def get_odd_tens_letters(num):
    if (num == 1 or num == 2):
        return 6
    if (num == 5 or num == 6):
        return 7
    if (num == 3 or num == 4 or num == 8 or num == 9):
        return 8
    else:
        return 9

sum = 0
last_sum = 0
for i in range(1,1001):
    (ones, tens, hundreds, thousands) = decompose_digit(i)
    # Case where you have an even hundred--Looks OK
    if (ones == 0 and tens == 0 and hundreds != 0):
        sum += get_num_letters(hundreds) + 7
        
    # Case where you have even tens with hundreds--Looks OK
    if (ones == 0 and tens != 0 and hundreds > 0):
        sum += get_num_letters(hundreds) + 10 + get_tens_letters(tens)

    # Case where you have hundreds > 0 tens == 0, ones
    if (ones != 0 and tens == 0 and hundreds != 0):
        sum += get_num_letters(hundreds) + 10 + get_num_letters(ones)
        
    # Case where you have non even tens, hundreds, ones
    if (ones != 0 and tens != 0 and hundreds != 0):
        if(tens == 1):
            sum += get_num_letters(hundreds) + 10 + get_odd_tens_letters(ones)
        else:
            sum += get_num_letters(hundreds) + 10 + get_tens_letters(tens) + get_num_letters(ones)
        
    # Case where you have even tens with no hundreds--Looks OK
    if (hundreds == 0 and tens != 0 and ones == 0):
        sum += get_tens_letters(tens)
        
    # Case where you have 100 > num > 11
    if (hundreds == 0 and tens != 0 and ones != 0):
        if(tens == 1):
            sum += get_odd_tens_letters(ones)
        else:
            sum += get_tens_letters(tens) + get_num_letters(ones)

    # Case where you have 10 > num > 0
    if (hundreds == 0 and tens == 0 and ones != 0):
        sum += get_num_letters(ones)

    if (thousands == 1):
        sum += 11

'''    print(i)
    print(sum)
    print(sum - last_sum)
    print('\n')
    last_sum = sum '''
        
print (sum)   
