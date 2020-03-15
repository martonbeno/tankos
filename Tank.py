from Object import *
from Bullet import *
from functions import *

TANK_HEIGHT = 75
TANK_WIDTH = 50
TANK_LOAD_TIME = 1000 #milliseconds
TANK_IMAGE_FILE = "red.png"

class Tank(Object):
	def __init__(self, x, y, born, color="black"):
		super().__init__(x, y, TANK_WIDTH, TANK_HEIGHT, born=born, color=color)
		self.type = "tank"
		self.load_time = TANK_LOAD_TIME
		self.image_file = TANK_IMAGE_FILE
		self.last_shot = born - self.load_time - 1 #it can shoot instantly
		self.can_shoot = True
	
	def shoot(self, time):
		self.last_shot = time
		
		bx = self.x + cos(self.angle)*(self.height + BULLET_WIDTH + 2)/2
		by = self.y + sin(self.angle)*(self.height + BULLET_WIDTH + 2)/2
		
		bullet_pos = bx, by
		
		return Bullet(x=bx, y=by, angle=self.angle, born=time, tank=self)
	
	
	# @Override
	def collide(self, other):
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
		
		return False