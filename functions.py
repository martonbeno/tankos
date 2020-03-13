from math import sqrt, fabs

def distance(point1, point2):
	# two tuples with (x,y) coordinates
	a = fabs(point1[0] - point2[0])
	b = fabs(point1[1] - point2[1])
	return sqrt(a**2 + b**2)
	
def line_point_collision(line, point, eps = 1):
	# line is a list of tuples with coordinates
	d1 = distance(line[0], point)
	d2 = distance(line[1], point)
	d3 = distance(line[0], line[1])
	return d1 + d2 - d3 <= eps