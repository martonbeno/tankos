from Object import Object

WALL_LENGTH = 50
WALL_THICKNESS = 5

class Wallside(Object):
	def __init__(self, center_x, center_y, width, height, allignment):
		
		#úgy működik jól, ha kicseréljük a height-ot a width-tel (ugyanígy az allignment is fordítva van)
		super().__init__(center_x, center_y, height, width, born=0, color="gray", type="wallside")
		self.allignment = allignment
		

def new_wall(x, y, sides): #0: up, 1: right, 2: down, 3: left
	ret = []
	
	if sides[0]:
		allignment = "vertical"
		width = WALL_LENGTH
		height = WALL_THICKNESS
		center_x = x + WALL_LENGTH/2
		center_y = y + WALL_THICKNESS/2
		ret.append(Wallside(center_x, center_y, width, height, allignment))
		
	if sides[1]:
		allignment = "horizontal"
		width = WALL_THICKNESS
		height = WALL_LENGTH
		center_x = x + WALL_LENGTH - WALL_THICKNESS/2
		center_y = y + WALL_LENGTH/2
		ret.append(Wallside(center_x, center_y, width, height, allignment))
	
	if sides[2]:
		allignment = "vertical"
		width = WALL_LENGTH
		height = WALL_THICKNESS
		center_x = x + WALL_LENGTH/2
		center_y = y + WALL_LENGTH - WALL_THICKNESS/2
		ret.append(Wallside(center_x, center_y, width, height, allignment))
	
	if sides[3]:
		allignment = "horizontal"
		width = WALL_THICKNESS
		height = WALL_LENGTH
		center_x = x + WALL_THICKNESS/2
		center_y = y + WALL_LENGTH/2
		ret.append(Wallside(center_x, center_y, width, height, allignment))
	
	return ret






