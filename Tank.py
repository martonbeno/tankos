from Rectangle import *
from Bullet import *

TANK_WIDTH = 50
TANK_HEIGHT = 75
TANK_LOAD_TIME = 1000 #milliseconds

class Tank(Rectangle):
	def __init__(self, x, y, born, color="black"):
		super().__init__(x, y, TANK_WIDTH, TANK_HEIGHT, born=born, color=color)
		self.type = "tank"
		self.load_time = TANK_LOAD_TIME
		self.last_shot = born - self.load_time - 1 #it can shoot instantly
	
	def shoot(self, time):
		self.last_shot = time
		
		bx = self.x + cos(self.angle)*(TANK_HEIGHT + BULLET_HEIGHT)/2
		by = self.y + sin(self.angle)*(TANK_HEIGHT + BULLET_HEIGHT)/2
		
		bullet_pos = bx, by
		
		return Bullet(x=bullet_pos[0], y=bullet_pos[1], angle=self.angle, born=time)