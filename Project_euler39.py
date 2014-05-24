'''Integer right triangles
Problem 39
If p is the perimeter of a right angle triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?'''


best = 3
current = 0
for perim in range(3, 1001):
	for x in range(1, perim):
		for y in range(1, perim):
			for z in range(1, perim):
				if x + y + z == perim:
					current +=0
	
	if current > best:
		best = perim
		
	if perim % 50 == 0:
		print('Current value of p is ', perim)
		
print('The value of p with max solutions is ', best)