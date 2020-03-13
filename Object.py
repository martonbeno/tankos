from math import sin, cos, asin, sqrt, pi, inf, fabs
from functions import *

class Object:
	def __init__(self, x, y, width, height, born, angle=0, color="black", name="Object"):
		self.x, self.y = x, y
		self.width, self.height = width, height
		self.born = born #time it was created (in milliseconds)
		self.angle = angle
		self.color = color
		self.name = name
		self.d = sqrt(height**2 + width**2)
		self.gamma = asin(width/self.d)
		self.type = None
		self.is_alive = True
		self.lifespan = inf
	
	def kill(self):
		self.is_alive = False
		print("au meghaltam")
	
	def get_corners(self):
		angle = self.angle
		gamma = self.gamma
		A = (self.x + (self.d/2)*cos(angle+gamma), self.y + (self.d/2)*sin(angle+gamma))
		B = (self.x + (self.d/2)*cos(angle-gamma), self.y + (self.d/2)*sin(angle-gamma))
		C = (self.x + (self.d/2)*cos(angle+gamma-pi), self.y + (self.d/2)*sin(angle+gamma-pi))
		D = (self.x + (self.d/2)*cos(angle-gamma+pi), self.y + (self.d/2)*sin(angle-gamma+pi))
		return [A, B, C, D]
		
	
	
	def rotate(self, deg):
		self.angle = (self.angle + deg) % (2*pi)

	def move(self, dir, dist):
		if dir == "forward":
			self.x += cos(self.angle)*dist
			self.y += sin(self.angle)*dist
		elif dir == "backwards":
			self.x -= cos(self.angle)*dist
			self.y -= sin(self.angle)*dist
		else:
			raise ValueError("dir has to be one of these: forward backwards\ncan not be " + dir)
	
	def __str__(self):
		return "{}\n---\ntype:{}\nx:{}\ny:{}\nself.angle:{}\ncorners:{}\nborn:{}".format(
			self.name,
			self.type,
			self.x,
			self.y,
			self.angle,
			self.get_corners(),
			self.born
		)
		
	def collide(self, other):
		if self.type == "bullet":
			if other.type == "tank":
				corners = other.get_corners()
				point = (self.x, self.y)
				a = (corners[0], corners[1])
				b = (corners[1], corners[2])
				c = (corners[2], corners[3])
				d = (corners[3], corners[0])
				return line_point_collision(a, point) or line_point_collision(b, point)\
					or line_point_collision(c, point) or line_point_collision(d, point)
					
		elif self.type == "tank":
			if other.type == "bullet":
				corners = self.get_corners()
				point = (other.x, other.y)
				a = (corners[0], corners[1])
				b = (corners[1], corners[2])
				c = (corners[2], corners[3])
				d = (corners[3], corners[0])
				return line_point_collision(a, point) or line_point_collision(b, point) or line_point_collision(c, point) or line_point_collision(d, point)
			elif other.type == "tank":
				return False
		