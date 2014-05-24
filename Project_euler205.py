'''Dice Game
Problem 205
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. 
The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? 
Give your answer rounded to seven decimal places in the form 0.abcdefg'''

from Functions import runtime
import random, time
from random import randint

start_time = time.clock()
random.seed()

pete_win = 0
cube = 0
tetra = 0
num_iter = 500000000
for iteration in range(num_iter):
		cube = randint(1,6)
		tetra = randint(1,4)
		
		if tetra > cube:
			pete_win += 1
		
print('The percentage is ', '{:.8f}'.format(pete_win/num_iter))
runtime(start_time)