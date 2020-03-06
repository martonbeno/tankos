from Rectangle import Rectangle
from Bullet import Bullet

TANK_WIDTH = 50
TANK_HEIGHT = 100
TANK_LOAD_TIME = 1000 #milliseconds

class Tank(Rectangle):
	def __init__(self, x, y, born, color="black"):
		super().__init__(x, y, TANK_WIDTH, TANK_HEIGHT, born=born, color=color)
		self.type = "tank"
		self.load_time = TANK_LOAD_TIME
		self.last_shot = born - self.load_time - 1 #it can shoot instantly
	
	def shoot(self, time):
		self.last_shot = time
		return Bullet(x=self.x, y=self.y, angle=self.angle, born=time)