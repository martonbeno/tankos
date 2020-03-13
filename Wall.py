from Object import Object

WALL_LENGTH = 100
WALL_WIDTH = 5

class Wall:
	def __init__(self, x, y, sides):
		self.x = x
		self.y = y
		self.sides = sides # sides expects a list with 4 boolean variables
		self.type = "wall"
		
	def get_sides(self):
		walls = []
		if self.sides[0]:
			walls.append(Object(self.x, self.y, WALL_WIDTH, WALL_LENGTH, 0))
		if self.sides[1]:
			walls.append(Object(self.x, self.y, WALL_LENGTH, WALL_WIDTH, 0))
		if self.sides[2]:
			walls.append(Object(self.x + WALL_LENGTH - WALL_WIDTH, self.y, WALL_WIDTH, WALL_LENGTH, 0))
		if self.sides[3]:
			walls.append(Object(self.x, self.y + WALL_LENGTH - WALL_WIDTH, WALL_LENGTH, WALL_WIDTH, 0))
		return walls