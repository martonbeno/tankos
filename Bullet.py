from Object import Object
from math import cos, sin

BULLET_WIDTH = 10
BULLET_HEIGHT = 10
BULLET_SPEED = 10
BULLET_LIFESPAN = 10000 # milliseconds

class Bullet(Object):
	def __init__(self, x, y, born, angle, tank):
		super().__init__(x, y, BULLET_WIDTH, BULLET_HEIGHT, born=born, angle=angle, color="black")
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