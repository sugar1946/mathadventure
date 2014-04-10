import spyral
import random
import math
import Walls
import Character
WIDTH = 600
HEIGHT = 600
BG_COLOR = (255,255,255)
BLACK = (0, 0, 255)
SIZE = (WIDTH, HEIGHT)
SIZE2 = (WIDTH/2, HEIGHT/2)
WALL_LIST = []
class Board(spyral.Scene):
	text = '';
	def __init__(self, *args, **kwargs):
	
		spyral.Scene.__init__(self, SIZE)
		spyral.event.register("system.quit", spyral.director.pop) 
		spyral.event.register("input.keyboard.down.q", spyral.director.pop)
	
	def setCharacter(self,character):
		self.player = character	
	
	def setBackGround(self,imagePath):
		self.background = spyral.Image(filename=imagePath)

	def setWalls(self,quadrantRow,quadrantColumn):
		if(quadrantRow == 0 and quadrantColumn == 0):
			wall = Walls.Walls(self)
			WALL_LIST.append(wall.wallTopHalf('Left'))
			wall = Walls.Walls(self)
			WALL_LIST.append(wall.wallTopHalf('Right'))
			wall = Walls.Walls(self)
			WALL_LIST.append(wall.wallBottomHalf('Left'))
			wall = Walls.Walls(self)
			WALL_LIST.append(wall.wallBottomHalf('Right'))
			wall = Walls.Walls(self)
			WALL_LIST.append(wall.wallLeftHalf('Top'))
			wall = Walls.Walls(self)
			WALL_LIST.append(wall.wallLeftHalf('Bottom'))
			wall = Walls.Walls(self)
			WALL_LIST.append(wall.wallRightHalf('Top'))
			wall = Walls.Walls(self)
			WALL_LIST.append(wall.wallRightHalf('Bottom'))


		
