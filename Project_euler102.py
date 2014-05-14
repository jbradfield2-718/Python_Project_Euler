''' Project Euler Triangle containment
Problem 102
Three distinct points are plotted at random on a Cartesian plane, 
for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file 
containing the co-ordinates of one thousand "random" triangles, find the number of triangles 
for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above. '''
import Functions
import time


def slope(x1,x2, y1, y2):
	return (y1 - y2)/(x1 - x2)
	
def y_intercept(m, x, y):
	return y - m*x

def within_line(int, y1, y2):
	if y1 > y2:
		if int < y1 and int > y2:
			return True
	else:
		if int < y2 and int > y1:
			return True
		return False

# Determines if triangle formed by the points encloses the origin
def triangle(x1,y1,x2,y2,x3,y3):
	if x1 < 0 and x2 < 0 and x3 < 0 or x1 > 0 and x2 > 0 and x3 > 0:
		return False
	if y1 < 0 and y2 < 0 and y3 < 0 or y1 > 0 and y2 > 0 and y3 > 0:
		return False
		
	m1 = slope(x1,x2,y1,y2)
	m2 = slope(x1,x3,y1,y3)
	m3 = slope(x2,x3,y2,y3)
	b1 = y_intercept(m1,x1,y1)
	b2 = y_intercept(m2,x3,y3)
	b3 = y_intercept(m3,x2,y2)
	num_above = 0
	num_below = 0
	
	test1 = within_line(b1,y1,y2)
	#print(b1,y1,y2,test1)
	
	if test1 == True:
		if b1 > 0:
			num_above += 1
		else:
			num_below += 1
	test2 = within_line(b2,y1,y3)
	#print(b2,y1,y3,test2)
	
	if test2 == True:
		if b2 > 0:
			num_above += 1
		else:
			num_below += 1
	if test1 == False and test2 == False:
		return False
	test3 = within_line(b3,y2,y3)
	#print(b3,y2,y3,test3)
	
	if test3 == True:
		if b3 > 0:
			num_above += 1
		else:
			num_below += 1
	#print(num_above,num_below)
	#a = input()
	if num_above + num_below < 2:
		return False
	if num_above == 1 and num_below == 1:
		return True
	else:
		return False
	
	
start = time.clock()
x1 = 0
x2 = 0
x3 = 0
y1 = 0
y2 = 0
y3 = 0

''' Need to determine if origin is in triangle.  If this is the case, then the y intercept of 2 of the 
	lines which enclose the triangle will be within the upper and lower y bounds formed by the points at
	the vertices. '''

ls = Functions.import_csv('triangles.txt')
enc_origin = []
num = 0


for coords in ls:
	x1 = int(coords[0])
	y1 = int(coords[1])
	x2 = int(coords[2])
	y2 = int(coords[3])
	x3 = int(coords[4])
	y3 = int(coords[5])
	#print('current coords under test...',coords)
	test = triangle(x1,y1,x2,y2,x3,y3)
	if test == True:
		num += 1
	

print('Number of triangles enclosing origin ',num)
Functions.runtime(start)