from Object import Object

WALL_LENGTH = 100
WALL_THICKNESS = 5

class Wallside(Object):
	def __init__(self, x, y, allignment):
		
		self.allignment = allignment
		if allignment is "horizontal":
			width = WALL_LENGTH
			height = WALL_THICKNESS
		elif allignment is "vertical":
			width = WALL_THICKNESS
			height = WALL_LENGTH
		else:
			raise ValueError("allignment has to be either 'horizontal' or 'vertical', can not be '" + str(allignment))
		
		# calculate center
		center_x = x + width/2
		center_y = y + height/2
		
		super().__init__(center_x, center_y, width, height, born=0, color="gray", type="wallside")

def new_wall(x, y, sides):	
	ret = []
	for i, is_real_side in enumerate(sides):
		if is_real_side:
			allignment = "horizontal" if i in [0,2] else "vertical"
			wallside = Wallside(x, y, allignment)
			ret.append(wallside)
	return ret









