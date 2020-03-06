from Rectangle import Rectangle

BULLET_WIDTH = 10
BULLET_HEIGHT = 10

class Bullet(Rectangle):
	def __init__(self, x, y, born, angle):
		super().__init__(x, y, BULLET_WIDTH, BULLET_HEIGHT, born=born, angle=angle, color="black")
		self.type = "bullet"