import math

class Object:
	def __init__(self, x, y, height, width, name="object"):
		self.x, self.y = x, y
		self.width, self.height = width, height
		self.alpha = 0
		self.name = name
	
	def get_corners_unrotated(self):
		return [(self.x+self.width//2, self.y-self.height//2),
				(self.x+self.width//2, self.y+self.height//2),
				(self.x-self.width//2, self.y+self.height//2),
				(self.x-self.width//2, self.y-self.height//2)]
	
	def get_corners(self):
		return self.get_corners_unrotated() #Ádám, ezt a sort töröld ki
	
	def rotate(self, deg):
		self.alpha = (self.alpha + deg) % 360

	def move(self, dir, dist):
		if dir == "up":
			self.y -= dist
		elif dir == "down":
			self.y += dist
		else:
			raise ValueError("dir has to be one of these: up down")
	
	def __str__(self):
		return "{}\n---\nx:{}\ny:{},alpha:{}\ncorners:{}\n".format(self.name, self.x, self.y, self.alpha, self.get_corners_unrotated())


if __name__ == "__main__":
	o = Object((100,100), 20, 50)
	