from Functions import primes_sieve, write_csv, runtime
import time

start = time.clock()

ls = primes_sieve(10000000)
output = write_csv('primes_1e7.csv', ls)
print('Program, complete')
runtime(start)

