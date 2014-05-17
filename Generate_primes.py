from Functions import primes_sieve, write_csv, runtime
import time

start = time.clock()

ls = primes_sieve(999999)
output = write_csv('primes_1e6.csv', ls)
print('Program, complete')
runtime(start)

