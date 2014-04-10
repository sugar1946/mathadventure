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
		spyral.event.register("director.update", self.update)

	def update(self,delta):
		for wall in WALL_LIST:
			self.player.collide_wall(wall)
	
	def setCharacter(self,character):
		self.player = character
		character.setKeyBoardCommands(self)	
	
	def setBackGround(self,imagePath):
		self.background = spyral.Image(filename=imagePath)

	def setWalls(self,quadrantRow,quadrantColumn):
		if(quadrantRow == 0 and quadrantColumn == 0):
			wall = Walls.Walls(self)
			wall.wallTopHalf('Left')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallTopHalf('Right')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallBottomHalf('Left')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallBottomHalf('Right')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallLeftHalf('Top')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallLeftHalf('Bottom')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallRightHalf('Top')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallRightHalf('Bottom')
			WALL_LIST.append(wall)



		
