from Object import Object
from math import cos, sin
from functions import *

BULLET_HEIGHT = 10
BULLET_WIDTH = 10
BULLET_SPEED = 10
BULLET_LIFESPAN = 10000 # milliseconds

class Bullet(Object):
	def __init__(self, x, y, born, angle, tank):
		super().__init__(x, y, BULLET_HEIGHT, BULLET_WIDTH, born=born, angle=angle, color="black")
		self.type = "bullet"
		self.vx = BULLET_SPEED*cos(self.angle)
		self.vy = BULLET_SPEED*sin(self.angle)
		self.lifespan = BULLET_LIFESPAN
		self.tank = tank
		
	def bullet_move(self):
		self.x += self.vx
		self.y += self.vy
	
	def bounce(self, dir):
		if dir == "horizontal":
			self.vx *= -1
		elif dir == "vertical":
			self.vy *= -1
	
	# @Override
	def collide(self, other):
		if other.type in ["tank", "wallside"]:
			corners = other.get_corners()
			point = (self.x, self.y)
			a = (corners[0], corners[1])
			b = (corners[1], corners[2])
			c = (corners[2], corners[3])
			d = (corners[3], corners[0])
			return line_point_collision(a, point) or line_point_collision(b, point)\
				or line_point_collision(c, point) or line_point_collision(d, point)
		
		return False