from math import sin, cos, asin, sqrt, pi

class Object:
	def __init__(self, x, y, height, width, name="object"):
		self.x, self.y = x, y
		self.width, self.height = width, height
		self.alpha = 0
		self.name = name
		self.d = sqrt(height**2 + width**2)
		self.gamma = asin(width/self.d)
	
	def get_corners_unrotated(self):
		return [(self.x+self.width//2, self.y-self.height//2),
				(self.x+self.width//2, self.y+self.height//2),
				(self.x-self.width//2, self.y+self.height//2),
				(self.x-self.width//2, self.y-self.height//2)]
	
	def get_corners(self):
		angle = self.alpha
		gamma = self.gamma
		A = (self.x + (self.d/2)*cos(angle+gamma), self.y + (self.d/2)*sin(angle+gamma))
		B = (self.x + (self.d/2)*cos(angle-gamma), self.y + (self.d/2)*sin(angle-gamma))
		C = (self.x + (self.d/2)*cos(angle+gamma-pi), self.y + (self.d/2)*sin(angle+gamma-pi))
		D = (self.x + (self.d/2)*cos(angle-gamma+pi), self.y + (self.d/2)*sin(angle-gamma+pi))
		return [A, B, C, D]
	
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
	
