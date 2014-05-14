''' Project Euler Problem 95
    Amicable Chains -- Find the smallest member of the longest
    amicable chain with no element > 1e6
'''
import math
import time

start=time.clock()
current_runtime = start

ls = []
master_list = []
fail_list = []
def find_sum_divisors(num):
    sum = 0
    start = math.ceil(num/2)

    for i in range(start,0,-1):
        if (num % i == 0):
            sum += i
    return sum

def runtime():
    return time.clock() - current_runtime


num = 200
current = num

while (num < 1e6):
    current = num
    count = 0
    ls = []
    ls.append(num)
    #print("Current number is...",num)
    while (True):
        current = find_sum_divisors(current)
        
        if (current in fail_list):
            break
        
        if (count == 50):
            break
        
        if (current > 1e6 or current == 1):
            for i in range(0,len(ls)):
                if(ls[i] not in fail_list):
                    fail_list.append(ls[i])
            ls = []
            break                                  # breaks from inner loop as current element > 1e6
        
        if (current <= 1e6):
            ls.append(current)
            
        if (current == num):
            tp = len(ls), min(ls)
            master_list.append( tp )      # adds length of list and minimum element to master list
            print(tp)
            ls = []
            break

        count += 1

    num += 1
    if( (runtime() - current_runtime) > 5 ):
        print("Calculating...current runtime ", runtime() - start, "seconds.")
        current_runtime = runtime() - current_runtime
    if (num % 1000 == 0):
        print("Current number under test...",num)

max_len = 0
min_num = 0
for i in range(0, len(master_list)):
    if( master_list[i][0] > max_len ):
        max_len = master_list[i][0]
        min_num = master_list[i][1]

runtime = time.clock()-start
print(master_list)
print("The maximum list length is ", max_len -1)
print("The minimum item length is ", min_num)
print ("The calculation time was",runtime," seconds.")
