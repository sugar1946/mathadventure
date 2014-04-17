import spyral
import random
import math
import Walls
import Character
import Monster
import Item
import Question

WIDTH = 1200
HEIGHT = 900

BG_COLOR = (255,255,255)
BLACK = (0, 0, 255)
SIZE = (WIDTH, HEIGHT)
SIZE2 = (WIDTH/2, HEIGHT/2)
WALL_LIST = []
##ENEMY_LIST = []
ITEM_LIST = []

class Board(spyral.Scene):
    text = ''
    ##self.ENEMY_LIST = []
    ##enemy = []
    def __init__(self, *args, **kwargs):
        spyral.Scene.__init__(self, SIZE)
        # self.monster = Monster.Monster(self)
        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
        spyral.event.register('director.update', self.update)
        self.ENEMY_LIST = []

    def update(self,delta):
        for wall in WALL_LIST:
            self.player.collide_wall(wall)
            
        for enemy in self.ENEMY_LIST:
            enemy.collide_wall(wall)

        for item in ITEM_LIST:
            self.player.collide_item(item)



    def setCharacter(self,character):
		self.player = character
		character.setKeyBoardCommands(self)

    def setMonster(self):
        for i in range(4):
            monster = Monster.Monster(self)
            self.ENEMY_LIST.append(monster)
            monster.setUpdate(self)

              
		
    def setChestsandGems(self):
        WIDTH_COORD = range(110, (WIDTH/2)-90) + range((WIDTH/2)+90, WIDTH-110)
        HEIGHT_COORD = range(110, (HEIGHT/2) - 110) + range((HEIGHT/2) + 110, HEIGHT-110)

        for i in range(random.randint(1,3)):
            x = random.choice(WIDTH_COORD)
            y = random.choice(HEIGHT_COORD)

            for i in WIDTH_COORD:
                if (x-40 < i < x+40):
                    WIDTH_COORD.remove(i)
            for i in HEIGHT_COORD:
                if (y-40 < i < y+40):
                    HEIGHT_COORD.remove(i)
                
            ITEM_LIST.append(Item.Item(self,"chest", x, y))
            
        for i in range(random.randint(2,4)):
            x = random.choice(WIDTH_COORD)
            y = random.choice(HEIGHT_COORD)

            for i in WIDTH_COORD:
                if (x-40 < i < x+40):
                    WIDTH_COORD.remove(i)
            for i in HEIGHT_COORD:
                if (y-40 < i < y+40):
                    HEIGHT_COORD.remove(i)
            
            ITEM_LIST.append(Item.Item(self,"gem", x, y))
	
    def setBackGround(self,imagePath):
		self.background = spyral.Image(filename=imagePath)

    def setWalls(self,quadrantRow,quadrantColumn):
		if(quadrantRow == 0 and quadrantColumn == 0):
			wall = Walls.Walls(self)
			wall.wallTopFull()
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallBottomHalf('Left')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallBottomHalf('Right')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallLeftFull()
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallRightHalf('Top')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallRightHalf('Bottom')
			WALL_LIST.append(wall)
		
		elif((quadrantRow == 0 and quadrantColumn == 1) or (quadrantRow == 0 and quadrantColumn == 2)):
			wall = Walls.Walls(self)
			wall.wallTopFull()
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

		elif(quadrantRow == 0 and quadrantColumn == 3):
			wall = Walls.Walls(self)
			wall.wallTopFull()
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallBottomHalf('Left')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallBottomHalf('Right')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallRightFull()
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallLeftHalf('Top')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallLeftHalf('Bottom')
			WALL_LIST.append(wall)

		elif((quadrantRow == 1 and quadrantColumn == 0) or (quadrantRow == 2 and quadrantColumn == 0)):
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
			wall.wallLeftFull()
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallRightHalf('Top')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallRightHalf('Bottom')
			WALL_LIST.append(wall)

		elif(quadrantRow == 3 and quadrantColumn == 0):
			wall = Walls.Walls(self)
			wall.wallTopHalf('Left')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallTopHalf('Right')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallBottomFull()
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallLeftFull()
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallRightHalf('Top')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallRightHalf('Bottom')
			WALL_LIST.append(wall)

		elif((quadrantRow == 3 and quadrantColumn == 1) or (quadrantRow == 3 and quadrantColumn == 2)):
			wall = Walls.Walls(self)
			wall.wallTopHalf('Left')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallTopHalf('Right')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallBottomFull()
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

		elif(quadrantRow == 3 and quadrantColumn == 3):
			wall = Walls.Walls(self)
			wall.wallTopHalf('Left')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallTopHalf('Right')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallBottomFull()
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallLeftHalf('Top')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallLeftHalf('Bottom')
			WALL_LIST.append(wall)

			wall = Walls.Walls(self)
			wall.wallRightFull()
			WALL_LIST.append(wall)

		elif((quadrantRow == 1 and quadrantColumn == 3) or (quadrantRow == 2 and quadrantColumn == 3)):
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
			wall.wallRightFull()
			WALL_LIST.append(wall)

		elif((quadrantRow == 1 and quadrantColumn == 1) or (quadrantRow == 1 and quadrantColumn == 2) or (quadrantRow == 2 and quadrantColumn == 1) or (quadrantRow == 2 and quadrantColumn == 2)):
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
