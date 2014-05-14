''' Project Euler Prob 258: Lagged Fibonacci sequence
    A sequence is defined as:

    gk = 1, for 0 ≤ k ≤ 1999
    gk = gk-2000 + gk-1999, for k ≥ 2000.
    Find gk mod 20092010 for k = 1018. '''

import time
import Functions
start = time.clock()

n_1 = 1
n_2 = 1

def fibonacci(counter):
    global n_1
    global n_2
    num_iter = 2
    x = 0
    
    while(num_iter < counter):
        x = n_1 + n_2
        n_1 = n_2
        n_2 = x
        num_iter += 1
    return x

def Binet(x):
    a = ((1 + 5**0.5)/2.0) ** x
    b = ((1 - 5**0.5)/2.) ** x

    return round((5**-0.5)*(a - b))
    
num = int(1e6)
print("The ",num,"th fibonacci number is: ",Binet(num))
print(Functions.runtime(start))
