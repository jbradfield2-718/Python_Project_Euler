'''Goldbach's other conjecture
Problem 46
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?'''

from Functions import import_csv
import time

def get_twice_squares_ls(limit):
    ls =  []
    for i in range(1, limit):
        ls.append(2* i**2)
    return ls

start_time = time.clock
primes_ls = import_csv('primes_1e6.csv')
primes_ls = list(map(int, primes_ls))
twice_squares_ls = get_twice_squares_ls(1000)
ls_of_odds = []
last_composite = 9
print(twice_squares_ls)
input()

for composite in range(1, 1000000, 2):
    if composite in primes_ls:
        continue

    for prime in primes_ls:
        if prime > composite:
            continue

        for double_square in twice_squares_ls:
            if double_square > composite:
                continue
            if prime + double_square > composite:
                continue
            if prime + double_square == composite:
                desired_num = composite
                if composite > last_composite +2:
                    last_composite = composite
                    break

    if desired_num > 0:
        break


print('The lowest composite number is ', desired_num)
Functions.runtime(start_time)







