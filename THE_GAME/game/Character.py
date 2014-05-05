import spyral
import random
import math
import Question
import Monster
import HealthGUI
import sys
from spyral import Animation, easing
from fractions import Fraction 

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (255,255,255)
BLACK = (0, 0, 255)
SIZE = (WIDTH, HEIGHT)
SIZE2 = (WIDTH/2, HEIGHT/2)

class Character(spyral.Sprite):
    def __init__(self):
        score = 0
        self.current_image = '';
        self.health = 150
        self.keys = 0
        self.ownedItems = []
        self.fraction = Fraction(0)
        self.decimal = 0
        self.percent = 0

        self.hp = HealthGUI.HealthGUI()



    def setAnimationArray(self,animationPath):
        data=[]                               # will hold the lines of the file
        with open(animationPath,'rU') as fin:
            for line in fin:                  # for each line of the file
                line=line.strip()             # remove CR/LF
                if line:                      # skip blank lines
                    data.append(line)
        return data

    # Character animations
    def setAnimations(self,scene,animation_array):
		#animationArray being passed in to the setAnimations function has setup:
		#animation_array[0] = right movement file path
		#animation_array[1] = right stop image path
		#animation_array[2] = left movement file path
		#animation_array[3] = left stop image path
		#animation_array[4] = up movement file path
		#animation_array[5] = up stop image path
		#animation_array[6] = down movement path
		#animation_array[7] = down stop image path

        # right walk animation sequence
        if(animation_array[0] != ''):
            right = self.setAnimationArray(animation_array[0])
            images = [spyral.Image(filename=f) for f in right]
            #right stop animation sequence
            stopR = [spyral.Image(filename=animation_array[1])]
            self.animation = Animation('image', easing.Iterate(images), duration = 1, loop=True)
            self.stop_r = Animation('image', easing.Iterate(stopR), duration = 1)
        
        # left walk animation sequence
        if(animation_array[2] != ''):
            left = self.setAnimationArray(animation_array[2])
            images2 = [spyral.Image(filename=f) for f in left]
            #left stop animation sequence
            stopL = [spyral.Image(filename=animation_array[3])]
            self.animation2 = Animation('image', easing.Iterate(images2), duration = 1, loop=True)
            self.stop_l = Animation('image', easing.Iterate(stopL), duration = 1)

        # down walk animation sequence
        if(animation_array[4] != ''):
            up = self.setAnimationArray(animation_array[4])
            images3 = [spyral.Image(filename=f) for f in up]
            #up stop animation sequence
            stopU = [spyral.Image(filename=animation_array[5])]
            self.animation3 = Animation('image', easing.Iterate(images3), duration = 1, loop=True)
            self.stop_u = Animation('image', easing.Iterate(stopU), duration = 1)


    def setScene(self,scene):
        super(Character, self).__init__(scene)

    
    def setImage(self,imagePath):
        #"game/images/stick.png"
        self.current_image = imagePath
        self.image = spyral.Image(filename=imagePath)
        self.anchor = "center"
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.moving = False 
        self.vel = 100
        self.hp.setImage(self.health)
        
    def damage(self):
        if (self.health - 10 >= 0):
            self.health-=10
            self.hp.sub(self.health)

    def setKeyBoardCommands(self,scene):
        # Key down
        spyral.event.register("input.keyboard.down.left", self.move_left)
        spyral.event.register("input.keyboard.down.right", self.move_right)
        spyral.event.register("input.keyboard.down.down", self.move_down)
        spyral.event.register("input.keyboard.down.up", self.move_up)
        spyral.event.register("input.keyboard.down.y", self.changeImage)
        spyral.event.register("input.keyboard.down.g", self.grab)

        # Key up
        spyral.event.register("input.keyboard.up.left", self.stop_move)
        spyral.event.register("input.keyboard.up.right", self.stop_move)
        spyral.event.register("input.keyboard.up.down", self.stop_move)
        spyral.event.register("input.keyboard.up.up", self.stop_move)
        #spyral.event.register("input.keyboard.up.g", self.stop_move)
        spyral.event.register('director.update', self.update)

        self.hp.setKeyBoardCommands(scene)

    def setScene(self,scene,row,column):
        super(Character,self).__init__(scene)
        self.sceneRow = row
        self.sceneColumn = column
        self.hp.setScene(scene)

    def setSceneMatrix(self,matrix):
        self.sceneMatrix = matrix

    def leavingScene(self):
        row = self.sceneRow
        column = self.sceneColumn
        distance = 100
        if(self.x < 0 and self.sceneColumn != 0):
            spyral.director.replace(self.sceneMatrix[row][column - 1])
            self.sceneMatrix[row][column - 1].setCharacter(self,self.ani_array)
            self.setScene(self.sceneMatrix[row][column - 1],row,column - 1)
            #self.sceneMatrix[row][column - 1].setCharacter(self,self.ani_array)
            #self.setImage(self.current_image)
            self.setImage("game/images/Animations/stop2l.bmp")
            self.x = WIDTH - distance
            
        elif(self.x > WIDTH and self.sceneColumn != 3):
            spyral.director.replace(self.sceneMatrix[row][column + 1])
            self.sceneMatrix[row][column + 1].setCharacter(self,self.ani_array)
            self.setScene(self.sceneMatrix[row][column + 1],row,column + 1)
            #self.sceneMatrix[row][column + 1].setCharacter(self,self.ani_array)
            #self.setImage(self.current_image)
            self.setImage("game/images/Animations/stop2.bmp")
            self.x = distance

        elif(self.y < 0 and self.sceneRow != 0):
            spyral.director.replace(self.sceneMatrix[row - 1][column])
            self.sceneMatrix[row - 1][column].setCharacter(self,self.ani_array)
            self.setScene(self.sceneMatrix[row - 1][column],row - 1,column)
            #self.sceneMatrix[row - 1][column].setCharacter(self,self.ani_array)
            #self.setImage(self.current_image)
            self.setImage("game/images/Animations/stop2.bmp")
            self.y = HEIGHT - distance

        elif(self.y > HEIGHT and self.sceneRow != 3):
            spyral.director.replace(self.sceneMatrix[row + 1][column])
            self.sceneMatrix[row + 1][column].setCharacter(self,self.ani_array)
            self.setScene(self.sceneMatrix[row + 1][column],row + 1,column)
            #self.sceneMatrix[row + 1][column].setCharacter(self,self.ani_array)
            #self.setImage(self.current_image)
            self.setImage("game/images/Animations/stop2.bmp")
            self.y = distance

    def move_left(self):
        self.moving = 'left'
        self.vel = 100
        self.stop_all_animations()
        self.animate(self.animation2)
    def move_right(self):
        self.moving = 'right'
        self.vel = 100
        self.stop_all_animations()
        self.animate(self.animation)
    def move_down(self):
        self.moving = 'down'
        self.vel = 100
        #self.stop_all_animations()
        #self.animate(self.animation4)
    def move_up(self):
        self.moving = 'up'
        self.vel = 100
        #self.stop_all_animations()
        #self.animate(self.animation3)
        
    def grab(self):
        self.stop_all_animations()
        #self.animate(self.grab_r)
        
    def stop_move(self):
        self.stop_all_animations()
        if (self.moving == 'right'):
            self.moving = False
            self.animate(self.stop_r)
            self.stop_animation(self.stop_r)
        elif (self.moving == 'left'):
            self.moving = False
            self.animate(self.stop_l)
            self.stop_animation(self.stop_l)
        else:
            self.moving = False
            self.stop_all_animations()


    def update(self, delta):
        if self.moving == 'left':
            self.x -= self.vel * delta
        elif self.moving == 'right':
            self.x += self.vel * delta
        elif self.moving == 'down':
            self.y += self.vel * delta
        elif self.moving == 'up':
            self.y -= self.vel * delta
        self.leavingScene()
        self.hp.setImage(self.health)

    def collide_wall(self,wall):
        if self.collide_sprite(wall):
            #self.vel = -self.vel
            #self.moving = False            
            if (self.moving == 'right'):
                self.x-= 4
                self.vel = 0
            elif (self.moving == 'left'):
                self.x+= 4
                self.vel = 0
            elif (self.moving == 'up'):
                self.y+= 4
                self.vel = 0
            elif (self.moving == 'down'):
                self.y-= 4
                self.vel = 0

    def collide_monster(self,monster):
        if self.collide_sprite(monster):
            if (self.moving == 'right'):
                self.x-= 2
                self.vel = 0
            elif (self.moving == 'left'):
                self.x+= 2
                self.vel = 0
            elif (self.moving == 'up'):
                self.y+= 2
                self.vel = 0
            elif (self.moving == 'down'):
                    self.y-= 2
                    self.vel = 0
            return True
 

    def collide_item(self, item):

        if (self.moving == 'right'):
            self.x-= 2
            self.vel = 0
        elif (self.moving == 'left'):
            self.x+= 2
            self.vel = 0
        elif (self.moving == 'up'):
            self.y+= 2
            self.vel = 0
        elif (self.moving == 'down'):
            self.y-= 2
            self.vel = 0
        return True


    def changeImage(self):
         self.current_image = "game/images/stick.bmp";
         x = self.x
         y = self.y
         self.setImage(self.current_image)
         self.x = x
         self.y = y
         
