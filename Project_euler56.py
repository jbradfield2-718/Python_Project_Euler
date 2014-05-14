''' Project Euler problem 56: Powerful Digit Sum
    A googol (10**100) is a massive number: one followed by one-hundred zeros;
    100**100 is almost unimaginably large: one followed by two-hundred zeros.
    Despite their size, the sum of the digits in each number is only 1.

    Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum? '''

import time
import Functions

start = time.clock()

best_sum = 0
test_num = 0
test_list = []

# Begin looking for possibles at 99**99, then decrement the exponent by one

for exponent in range(99, 89, -1):
    
    for base in range(99, 89, -1):
        test_num = base**exponent
        test_list = Functions.decompose_digit(test_num)
        test_num = 0

        for i in range(0, len(test_list)):
            test_num += test_list[i]

        if(test_num > best_sum):
            best_sum = test_num
            print("\nThe current best sum is ", best_sum)

        test_num = 0
        test_list = []
            
        
        
print("The greatest digital sum is ", best_sum)
print(Functions.runtime(start))
