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
import random
import math
import Door
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
DOOR_LIST = []

class ScoreSprite(spyral.Sprite):
    def __init__(self,scene,img,x,y):
        spyral.Sprite.__init__(self,scene)
        self.image = img
        self.x = x
        self.y = y


class FinalScreen(spyral.Sprite):
    def __init__(self,scene):
        spyral.Sprite.__init__(self,scene)
        self.image = spyral.Image(filename=('game/images/FianlScreen.bmp'))
        self.pos = (350,50)
        self.layer = 'top'
        

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
	'''
	def setButtomImage(self,item):
		image_up: item
		image_up_hovered: item
		image_up_focused: item
		image_down: item
		image_down_hovered: item
		image_down_focused: item
		nine_slice: True
	'''
	#answer_input = spyral.widgets.TextInput(100, "")
	store_button = spyral.widgets.Button("Store")
	whichButton = 1


class Board(spyral.Scene):
    text = ''
    
    ##self.self.ENEMY_LIST = []
    ##enemy = []
    def __init__(self, *args, **kwargs):
        spyral.Scene.__init__(self, SIZE)
        # self.monster = Monster.Monster(self)
        self.layers = ['bottom','top']
        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
        spyral.event.register('director.update', self.update)
        self.ENEMY_LIST = []

        self.fraction =''
        self.score = ''
        self.keys=''
        frozen = False




    def update(self,delta):
        self.showScore()
        self.showFraction()
        self.showKeys()
        self.healthTracker()
        for wall in WALL_LIST:
            self.player.collide_wall(wall)

        for door in DOOR_LIST:
            self.player.collide_door(door)

        for item in ITEM_LIST:
            if (self.player.collide_sprite(item)):
 
                if (item.name == 'chest'):

                    self.freezeMonster()
                    ##self.question = Q.Question(self)

                    self.question = Q.Question(self,self.player)

                    item.kill()
                elif (item.name == "gem"):
                    self.player.fraction += Fraction(item.top_number, item.bottom_number)
                    if (self.player.fraction == Fraction(1)):
                        key = Item.Item(self, "key")
                        key.setScene(self)

                        flag = True
                        while (flag == True):
                                w = random.randint(150,1050)
                                h = random.randint(100,800)
                                for enemy in self.ENEMY_LIST:
                                        x=enemy.x
                                        y=enemy.y
                                        if ((x-50<w<x+50)and(y-60<h<y+60)):
                                                flag == True
                                        else:
                                                flag == False

                                for item in ITEM_LIST:
                                        x = item.x
                                        y = item.y
                                        if(item.name == 'chest'):
                                                if ((x-20<w<x+105)and(y-80<h<y+20)):
                                                        flag == True
                                                else:
                                                        flag=False
                                        elif(item.name =='gem'):
                                                if((x-20<w<x+55)and(y-80<h<y+20)):
                                                        flag == True
                                                else:
                                                        flag=False
                                        
                                if (flag == False):
                                        key.setImage('game/images/key_converted.bmp',w,h)
                                        
                        ITEM_LIST.append(key)
                    elif (self.player.fraction > Fraction(1)):
                        self.player.fraction -= Fraction(1)
                    print 'fraction' + str(self.player.fraction)
                    item.kill()
                elif (item.name == 'key'):
                    item.kill()
                    self.player.keys += 1
                    print "keys = " + str(self.player.keys)



                
        for enemy in self.ENEMY_LIST:
            temp = self.ENEMY_LIST
            enemy.collide_wall(wall)
            enemy.collide_player(self.player)
            self.player.collide_monster(enemy)
            
            for item in ITEM_LIST:
                enemy.collide_item(item)
            for x in self.ENEMY_LIST:
                if(x != enemy):
                    enemy.collide_monster(x)
        num = len(self.ENEMY_LIST)
        n = random.randint(0,num-1)
        chance = random.random()

        if (chance <0.03):
                choices = ['up','down','left','right']
                choices.remove(self.ENEMY_LIST[n].direction)
                direction = random.choice(choices)
                self.ENEMY_LIST[n].direction = direction



        ##change the direction , during the move, the monster would change its direction by 30% possibil

            

    def healthTracker(self):
        if(self.player.health == 0):
            self.finalscreen = FinalScreen(self)
            self.player.kill()
            self.freezeMonster()


    ##def addMonster(self):
##        if (len(self.ENEMY_LIST)) <

        
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

		        
    def setCharacter(self,character,animation_array):
        self.player = character
        character.setAnimations(self,animation_array)
        character.setKeyBoardCommands(self)

    def setStoreButton(self):
        self.storeButton = StoreSetupForm(self)
        self.storeButton.store_button.x = WIDTH - 80
        self.storeButton.store_button.y = HEIGHT - 80
        spyral.event.register("form.StoreSetupForm.store_button.clicked",self.openStore)
	    #temp.setButtonImage("game/store/gem.bmp")

    def openStore(self,widget,form,value):
        store = Store.Store(self.player)
        store.setSceneReturn(self)
        spyral.director.push(store)

    def setDoor(self, qRow, qCol):
        # Testing door rendering
        if(qRow == 1 and qCol == 3):
            door = Door.Door(self)
            door.setImage("1")
            DOOR_LIST.append(door)

        if(qRow == 0 and qCol == 2):
            door = Door.Door(self)
            door.setImage("2")
            DOOR_LIST.append(door)
        
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
                for item in ITEM_LIST:
                        x = item.x
                        y = item.y
                        if (item.name == 'chest'):
                                if ((x-50 <= l <= x+140)and(y-125<= w <= y+65)):
                                        flag = False

                        if (item.name == 'gem'):
                                if ((x-55 <= l <= x+95)and(y-125<=w<=y+65)):
                                        flag = False

                for enemy in self.ENEMY_LIST:
                        x = enemy.x
                        y = enemy.y
                        if ((x-90 < l < x+90) and (y-120 < w < y +120)):
                                  flag = False
                                  
                if(flag==True):
                        monster = Monster.Monster(self,image,l,w)
                        #print ("the "+str(count) + " monster's x is "+ str(l))
                        #print ("the "+str(count) + " monster's y is "+ str(w))
                        self.ENEMY_LIST.append(monster)
                        monster.setUpdate(self)
                        count = count+1

                
                
 
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

    def addGem(self):
        WIDTH_COORD = range(30, (WIDTH/2)-150) + range((WIDTH/2)+60, WIDTH-120)
        HEIGHT_COORD = range(120, (HEIGHT/2) - 85) + range((HEIGHT/2) + 150, HEIGHT-30)
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

    def addChest(self):
        WIDTH_COORD = range(30, (WIDTH/2)-150) + range((WIDTH/2)+60, WIDTH-120)
        HEIGHT_COORD = range(120, (HEIGHT/2) - 85) + range((HEIGHT/2) + 150, HEIGHT-30)
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
        

