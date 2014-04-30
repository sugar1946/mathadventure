import spyral
import random
import math
import Walls
import Character
import Monster
import Item
import Question
import Q
import HealthGUI

WIDTH = 1200
HEIGHT = 900

BG_COLOR = (255,255,255)
BLACK = (0, 0, 255)
SIZE = (WIDTH, HEIGHT)
SIZE2 = (WIDTH/2, HEIGHT/2)
WALL_LIST = []
ENEMY_LIST = []
ITEM_LIST = []


class Board(spyral.Scene):
    text = ''
    ##self.ENEMY_LIST = []
    ##enemy = []
    def __init__(self, *args, **kwargs):
        spyral.Scene.__init__(self, SIZE)
        # self.monster = Monster.Monster(self)
        self.layers = ['top', 'bottom']
        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
        spyral.event.register('director.update', self.update)
        ENEMY_LIST = []

    def update(self,delta):

        for wall in WALL_LIST:
            self.player.collide_wall(wall)

        for item in ITEM_LIST:
            if (self.player.collide_sprite(item)):

            
    
        
        

                if (item.name == 'chest'):
                    #self.player.collide_item(item)
##                    self.question.setReturnScene(self)
##                    self.question.openQuestion(item)
                    self.question = Q.Question(self)
                    item.x = 90000
                elif (item.name == "gem"):
                    item.kill()


                
        for enemy in ENEMY_LIST:
            temp = ENEMY_LIST
            enemy.collide_wall(wall)
            enemy.collide_player(self.player)
            self.player.collide_monster(enemy)
            
            for item in ITEM_LIST:
                enemy.collide_item(item)
            for x in ENEMY_LIST:
                if(x != enemy):
                    enemy.collide_monster(x)
   
##    def setQuestion(self, question):
##        self.question = question
        
    def setCharacter(self,character):
        self.player = character
        character.setAnimations(self)
        character.setKeyBoardCommands(self)

    def setMonster(self):
        for i in range(4):
            monster = Monster.Monster(self)
            ENEMY_LIST.append(monster)
            monster.setUpdate(self)         
        
    def setchestsandgems(self):
        WIDTH_COORD = range(30, (WIDTH/2)-150) + range((WIDTH/2)+60, WIDTH-120)
        HEIGHT_COORD = range(120, (HEIGHT/2) - 85) + range((HEIGHT/2) + 150, HEIGHT-30)
        self.gems = []

        for i in range(random.randint(1,3)):
            x = random.choice(WIDTH_COORD)
            y = random.choice(HEIGHT_COORD)

            for i in WIDTH_COORD:
                if (x-95 < i and i < x+95):
                    WIDTH_COORD.remove(i)
            for i in HEIGHT_COORD:
                if (y-75 < i and i< y+75):
                    HEIGHT_COORD.remove(i)
                
	    item = Item.Item(self,"chest")
	    item.setScene(self)
	    item.setImage("game/images/chest.bmp",x,y)
	    ITEM_LIST.append(item)

        for i in range(random.randint(2,4)):
            x = random.choice(WIDTH_COORD)
            y = random.choice(HEIGHT_COORD)

            for i in WIDTH_COORD:
                if (x-40 < i < x+40):
                    WIDTH_COORD.remove(i)
            for i in HEIGHT_COORD:
                if (y-60 < i < y+60):
                    HEIGHT_COORD.remove(i)
            
	    item = Item.Item(self,"gem")
	    item.setScene(self)
	    item.setImage("game/images/gem.bmp",x,y)
	    self.gems.append(item)
	    item.setFraction()
        ITEM_LIST.extend(self.gems)
	    
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
        

