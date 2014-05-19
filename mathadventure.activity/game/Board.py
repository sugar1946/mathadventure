import spyral
import random
import math
import Walls
import Character
import Monster
import Item
import Store
import Q
import HealthGUI
import Door
#import PlayerSelectionScene
#import StartScene
import RestartScene
from fractions import Fraction
FONT_PATH = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

WIDTH = 1200
HEIGHT = 900

BG_COLOR = (255,255,255)
BLACK = (0, 0, 255)
SIZE = (WIDTH, HEIGHT)
SIZE2 = (WIDTH/2, HEIGHT/2)
WALL_LIST = []
##ENEMY_LIST = []
ITEM_LIST = []
#DOOR_LIST = []
GEMS_LIST =[]

class FinalScreen(spyral.Sprite):
    def __init__(self,scene):
        spyral.Sprite.__init__(self,scene)
        self.image = spyral.Image(filename=('game/images/lost.png'))
        self.pos = (150,50)
        self.layer = 'top'

    def killScene(self):
        self.kill()
        
class WinScreen(spyral.Sprite):
    def __init__(self,scene):
        spyral.Sprite.__init__(self,scene)
        self.image = spyral.Image(filename=('game/images/won.png'))
        self.pos = (150,50)
        self.layer = 'top'
        
    def killScene(self):
        self.kill()
        
class EndInstructions(spyral.Sprite):
    def __init__(self,scene):
        spyral.Sprite.__init__(self,scene)
        self.image = spyral.Image(filename=('game/images/end_instructions.png'))
        self.pos = (225,150)
        self.layer = 'top'
        spyral.event.register("input.keyboard.down.x", self.close)
        
    def close(self):
        self.kill()

    
                            
class ScoreSprite(spyral.Sprite):
    def __init__(self,scene,img,x,y):
        spyral.Sprite.__init__(self,scene)
        self.image = img
        self.x = x
        self.y = y


class FractionSprite(spyral.Sprite):
    def __init__(self,scene,img,x,y):
        spyral.Sprite.__init__(self,scene)
        self.image = img
        self.x = x
        self.y = y

class KeySprite(spyral.Sprite):
    def __init__(self,scene,img,x,y):
        spyral.Sprite.__init__(self,scene)
        self.image = img
        self.x = x
        self.y = y

class StoreSetupForm(spyral.Form):
	store_button = spyral.widgets.Button("Store")
	whichButton = 1

class RestartSetupForm(spyral.Form):
	restart_button = spyral.widgets.Button("Restart")
	whichButton = 2

class QuitSetupForm(spyral.Form):

	quit_button = spyral.widgets.Button("Quit")
	whichButton = 2



class Board(spyral.Scene):
    text = ''
    
    ##self.self.ENEMY_LIST = []
    ##enemy = []
    def __init__(self, *args, **kwargs):
        spyral.Scene.__init__(self, SIZE)
        # self.monster = Monster.Monster(self)
        self.layers = ['bottom','top']
        spyral.event.register("system.quit", spyral.director.quit)
        spyral.event.register("input.keyboard.down.q", spyral.director.quit)
        spyral.event.register('director.update', self.update)
        self.ENEMY_LIST = []
        self.ITEM_LIST = []
        self.DOOR_LIST = []
        self.EnemyNum = 4
        self.gem_index = 0
        self.enemyDeleteIndex = 5
        self.fraction =''
        self.score = ''
        self.keys=''
        self.finalscreen = ''
        self.winscreen = ''
        self.signal = 'close'
        frozen = False
           

    def update(self,delta):
        self.showScore()
        self.showFraction()
        self.showKeys()
        self.healthTracker()
        self.addMonster()
        for wall in WALL_LIST:
            self.player.collide_wall(wall)

        for door in self.DOOR_LIST:
            self.player.collide_door(self, door, self.player.keys)

        
        for item in self.ITEM_LIST:
            if (self.player.collide_sprite(item)):
                if (item.name == 'chest'):
                    self.freezeMonster()
                    self.question = Q.Question(self,self.player)
                    newList = []
                    for tempItem in  self.ITEM_LIST:
                        if(tempItem != item):
                            newList.append(tempItem)
                    self.ITEM_LIST = []
                    self.ITEM_LIST = newList    
                    #self.ITEM_LIST.remove(item)#remove self
                    item.kill()
                    
                elif (item.name == "gem"):
                    self.player.fraction += Fraction(item.top_number, item.bottom_number)
                    if (self.player.fraction == Fraction(1)):
                        self.player.keys += 1
			self.signal = 'open'
                        self.player.fraction = 0
                        
                    elif (self.player.fraction >= Fraction(1)):
                        self.player.fraction = 0;
                        #self.ITEM_LIST.remove(item)#remove self
                    newList = []
                    for tempItem in  self.ITEM_LIST:
                        if(tempItem != item):
                            newList.append(tempItem)
                    self.ITEM_LIST = []
                    self.ITEM_LIST = newList
                    item.kill()

                elif (item.name == "End Gem"):
                    if (item.fraction == GEMS_LIST[0] ):
                        GEMS_LIST.pop(0)
                        item.kill()
                        if (len(GEMS_LIST) == 0):
                            vortex = Item.Item(self, "vortex")
                            vortex.setScene(self)
                            vortex.setImage("game/images/blue_vortex.png",random.randint(30,WIDTH-120),random.randint(120,HEIGHT-30))
                            self.ITEM_LIST.append(vortex)
                    else:

                        GEMS_LIST.remove(item.fraction)
                        item.kill()
                        newgem = Item.Item(self,"End Gem")
                        newgem.setScene(self)
                        newgem.setImage("game/images/purplegem.png",random.randint(30,WIDTH-120),random.randint(120,HEIGHT-30))
                        newgem.setFraction()
                        GEMS_LIST.append(newgem.fraction)
                        GEMS_LIST.sort()
                        self.ITEM_LIST.append(newgem)
       
                elif (item.name == "vortex"):
                    item.kill()
                    self.player.kill()
                    self.winscreen = WinScreen(self)

        for enemy in self.ENEMY_LIST:
            #temp = self.ENEMY_LIST
            #index = self.ENEMY_LIST.index(enemy)
  
            for item in self.ITEM_LIST:
                enemy.collide_item(item)
            for x in self.ENEMY_LIST:
                if(x != enemy):
                    enemy.collide_monster(x)
            if(enemy.collide_player(self.player) == True):
                '''
                tempEnemyList = []
                for tempEnemy in self.ENEMY_LIST:
                    if(tempEnemy != enemy):
                        tempEnemyList.append(tempEnemy)
                #self.ENEMY_LIST = []
                #self.ENEMY_LIST = tempEnemyList
                '''
                enemy.kill()

        if (len(self.ENEMY_LIST) != 0):
            num = len(self.ENEMY_LIST)
            ##print ("num=len(self.E)")
            n = random.randint(0,num-1)
            chance = random.random()

            if (chance <0.03):
                    choices = ['up','down','left','right']
                    choices.remove(self.ENEMY_LIST[n].direction)
                    direction = random.choice(choices)
                    self.ENEMY_LIST[n].direction = direction

    def healthTracker(self):
        if(self.player.health == 0):
            if(self.finalscreen == ''):
                self.finalscreen = FinalScreen(self)
            self.player.kill()
            self.freezeMonster()
	    

    def setBoss(self):
        l = random.randint(160,1200-160)
        w = random.randint(150,900-125)
        monster = Monster.Monster(self)
        monster.setImage("game/images/Boss.png",l,w)
        monster.vel_y =150
        monster.vel_x = 150
        monster.setUpdate(self)
        self.ENEMY_LIST.append(monster)
		

    def addMonster(self):
        #temp = self.player.keys
        
        if (self.signal=='open'):
            for n in range(2):
                flag=True
            
            
                print ("add monster")
                while (flag==True):
                    l = random.randint(160,1200-160)
                    w = random.randint(150,900-125)
                
                
                    for item in self.ITEM_LIST:
                        x = item.x
                        y = item.y
                        if (item.name == 'chest'):
                                if ((x-50 <= l <= x+140)and(y-125<= w <= y+65)):
                                        flag = True
                                else:
                                        flag = False

                        if (item.name == 'gem'):
                                if ((x-55 <= l <= x+95)and(y-125<=w<=y+65)):
                                        flag = True
                                else:
                                        flag = False

                for enemy in self.ENEMY_LIST:
                        x = enemy.x
                        y = enemy.y
                        if ((x-90 < l < x+90) and (y-120 < w < y +120)):
                                    flag = True
                        else:
                                    flag=False
                if(flag==False):
                    
                   
                        if(self.player.image == "game/images/Animations/Boy/1.png"):
                            monster = Monster.Monster(self)
                            monster.setImage("game/images/m2_30_30.bmp",l,w)

                        else:
                            monster = Monster.Monster(self)
                            monster.setImage("game/images/m1_30_30.bmp",l,w)
                        
                        monster.vel_x = 70
                        monster.vel_y = 70
                        #print ("the "+str(count) + " monster's x is "+ str(l))
                        #print ("the "+str(count) + " monster's y is "+ str(w))
                        self.ENEMY_LIST.append(monster)
                        monster.setUpdate(self)
                        self.signal = 'close'
    
    def showScore(self):
        scoreFont = spyral.Font(FONT_PATH,36,(245,221,7))
        score_img = scoreFont.render("Score: "+str(self.player.totalScore))
        if(self.score != ''):
            self.score.kill()
        self.score = ScoreSprite(self,score_img,60,40)


    def showFraction(self):
        scoreFont = spyral.Font(FONT_PATH,36,(245,221,7))
        fraction_img = scoreFont.render("Fraction: "+str(self.player.fraction))
        if(self.fraction != ''):
            self.fraction.kill()
        self.fraction = FractionSprite(self,fraction_img,60,70)

    def showKeys(self):
        scoreFont = spyral.Font(FONT_PATH,36,(245,221,7))
        key_img = scoreFont.render("Keys: "+str(self.player.keys))
        if(self.keys != ''):
            self.keys.kill()
        self.keys = KeySprite(self,key_img,60,100)

		        
    def setCharacter(self,character,animation_array,isAlive):
        if (isAlive == True):
            character.setKeyBoardCommands(self)
        self.player = character
        character.setAnimations(self,animation_array)


    def Quit(self,widget,form,value):
        spyral.director.quit()
        

    def Restart(self,widget,form,value):

        if(self.finalscreen != ''):
            self.finalscreen.killScene()
            self.finalscreen = ''
        if(self.winscreen != ''):
            self.winscreen.killScene()
            self.winscreen = ''
        restart = RestartScene.Main()
        restart.setCharacter(self.player)
        spyral.director.replace(restart)
	#print "startScene has been created"
	#return



    def setRestartButton(self):

        self.restartButton = RestartSetupForm(self)
        self.restartButton.restart_button.x = WIDTH-80

        self.restartButton.restart_button.y = HEIGHT-160
        spyral.event.register("form.RestartSetupForm.restart_button.clicked",self.Restart)
	    #temp.setButtonImage("game/store/gem.bmp")

    def setQuitButton(self):
        self.quitButton = QuitSetupForm(self)
        self.quitButton.quit_button.x = WIDTH -80
        self.quitButton.quit_button.y = HEIGHT-240
		
        spyral.event.register("form.QuitSetupForm.quit_button.clicked",self.Quit)


    def setStoreButton(self):
        self.storeButton = StoreSetupForm(self)
        self.storeButton.store_button.x = WIDTH - 80
        self.storeButton.store_button.y = HEIGHT - 200
        spyral.event.register("form.StoreSetupForm.store_button.clicked",self.openStore)
	    #temp.setButtonImage("game/store/gem.bmp")

    def openStore(self,widget,form,value):
        self.freezeMonster()
        
        store = Store.Store(self.player)
        store.setSceneReturn(self)
        
        spyral.director.push(store)

    def setDoor(self, qRow, qCol):
        # Testing door rendering
        if(qRow == 1 and qCol == 3):
            door = Door.Door(self)
            door.setImage("1")
            self.DOOR_LIST.append(door)

        if(qRow == 0 and qCol == 2):
            door = Door.Door(self)
            door.setImage("2")
            self.DOOR_LIST.append(door)

    def setHealth(self):
        gui = HealthGUI.HealthGUI()
        gui.setKeyBoardCommands(self)

    def freezeMonster(self):
        for enemy in self.ENEMY_LIST:
                enemy.frozen = True
               

    def defreezeMonster(self):
        for enemy in self.ENEMY_LIST:
                enemy.frozen = False



    def setMonster(self,image):
 
        count = 0
        while (count < 4):
                l = random.randint(160,1200-160)
                w = random.randint(150,900-125)
                
                flag = True
                for item in self.ITEM_LIST:
                        x = item.x
                        y = item.y
                        if (item.name == 'chest'):
                                if ((x-50-100 <= l <= x+140+100)and(y-125-100<= w <= y+65+100)):
                                        flag = False

                        if (item.name == 'gem'):
                                if ((x-55-100 <= l <= x+95+100)and(y-125-100<=w<=y+65+100)):
                                        flag = False

                for enemy in self.ENEMY_LIST:
                        x = enemy.x
                        y = enemy.y
                        if ((x-90-100 < l < x+90+100) and (y-120-100 < w < y +120+100)):
                                  flag = False
                                  
                if(flag==True):
                        monster = Monster.Monster(self)
                        monster.setImage(image,l,w)
                        #print ("the "+str(count) + " monster's x is "+ str(l))
                        #print ("the "+str(count) + " monster's y is "+ str(w))
                        self.ENEMY_LIST.append(monster)
                        monster.setUpdate(self)
                        count = count+1



    def setchestsandgems2(self):
 
        count = 0
        while (count < 4):
                l = random.randint(160,1200-160)
                w = random.randint(150,900-125)
                
                flag = True
                for item in self.ITEM_LIST:
                        x = item.x
                        y = item.y
                        if (item.name == 'chest'):
                                if ((x-95 <= l <= x+95)and(y-75<= w <= y+75)):
                                        flag = False

                        if (item.name == 'gem'):
                                if ((x-95 <= l <= x+90)and(y-75<=w<=y+75)):
                                        flag = False

                
                                  
                if(flag==True):
						gem = Item.Item(self,"gem")
						gem.setScene(self)
						gem.setImage("game/images/gem.png",l,w)
	   					gem.setFraction()
						ITEM_LIST.append(gem)
						count = count +1   



		count = 0
		while (count < 4):
				l = random.randint(160,1200-160)
				w = random.randint(150,900-125)
                
				flag = True
				for item in self.ITEM_LIST:
						x = item.x
						y = item.y
						if (item.name == 'chest'):
							if ((x-95 <= l <= x+95)and(y-75<= w <= y+75)):
								flag = False

						if (item.name == 'gem'):
							if ((x-95 <= l <= x+90)and(y-75<=w<=y+75)):
								flag = False

                
                                  
				if(flag==True):
					chest = Item.Item(self,"chest")
					chest.setScene(self)
					chest.setImage("game/images/chest.bmp",l,w)
					chest.setFraction()
					ITEM_LIST.append(chest)
					count = count +1      
    
 
    def setchestsandgems(self):
        WIDTH_COORD = range(30, (WIDTH/2)-150) + range((WIDTH/2)+60, WIDTH-120)
        HEIGHT_COORD = range(120, (HEIGHT/2) - 85) + range((HEIGHT/2) + 150, HEIGHT-30)

        for i in range(random.randint(1,3)):
            x = random.choice(WIDTH_COORD)
            y = random.choice(HEIGHT_COORD)

            for i in WIDTH_COORD:
                if (x-95 < i and i < x+95):
                    WIDTH_COORD.remove(i)
            for i in HEIGHT_COORD:
                if (y-75 < i and i< y+75):
                    HEIGHT_COORD.remove(i)
                
	    chest = Item.Item(self,"chest")
	    chest.setScene(self)
	    chest.setImage("game/images/chest.bmp",x,y)
	    self.ITEM_LIST.append(chest)
	    

        for i in range(random.randint(2,4)):
            x = random.choice(WIDTH_COORD)
            y = random.choice(HEIGHT_COORD)

            for i in WIDTH_COORD:
                if (x-95 < i < x+95):
                    WIDTH_COORD.remove(i)
            for i in HEIGHT_COORD:
                if (y-75 < i < y+75):
                    HEIGHT_COORD.remove(i)
            
	    gem = Item.Item(self,"gem")
	    gem.setScene(self)
	    gem.setImage("game/images/redgem.png",x,y)

	    gem.setFraction()
	    self.ITEM_LIST.append(gem)#remove self
        
    def setEndGems(self):
        WIDTH_COORD = range(30, WIDTH-120)
        HEIGHT_COORD = range(120, HEIGHT-30)
        self.gems = []

        for i in range(8):
            x = random.choice(WIDTH_COORD)
            y = random.choice(HEIGHT_COORD)

            for i in WIDTH_COORD:
                if (x-50 < i < x+50):
                    WIDTH_COORD.remove(i)
            for i in HEIGHT_COORD:
                if (y-60 < i < y+60):
                    HEIGHT_COORD.remove(i)
            
            item = Item.Item(self,"End Gem")
            item.setScene(self)
            item.setImage("game/images/purplegem.png",x,y)
            item.setFraction()
            self.gems.append(item.fraction)
            self.ITEM_LIST.append(item)#remove self
                    
        GEMS_LIST.extend(sorted(self.gems))   
        self.end_instructions = EndInstructions(self)

    def setBackGround(self,imagePath):
        self.background = spyral.Image(filename=imagePath)

    def addChest(self):
        WIDTH_COORD = range(30, (WIDTH/2)-150) + range((WIDTH/2)+60, WIDTH-120)
        HEIGHT_COORD = range(120, (HEIGHT/2) - 85) + range((HEIGHT/2) + 150, HEIGHT-30)
        x = random.choice(WIDTH_COORD)
        y = random.choice(HEIGHT_COORD)   
        chest = Item.Item(self,"chest")
        chest.setScene(self)
        chest.setImage("game/images/chest.bmp",x,y)
        self.ITEM_LIST.append(chest)

    def addGem(self):
        WIDTH_COORD = range(30, (WIDTH/2)-150) + range((WIDTH/2)+60, WIDTH-120)
        HEIGHT_COORD = range(120, (HEIGHT/2) - 85) + range((HEIGHT/2) + 150, HEIGHT-30)
        x = random.choice(WIDTH_COORD)
        y = random.choice(HEIGHT_COORD)
        gem = Item.Item(self,"gem")
        gem.setScene(self)
        gem.setImage("game/images/gem.png",x,y)
        gem.setFraction()
        self.ITEM_LIST.append(gem)#remove self        

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
        

