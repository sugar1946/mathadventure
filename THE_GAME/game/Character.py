import spyral
import random
import math
import Question
import Monster
import sys
from spyral import Animation, easing
WIDTH = 1200
HEIGHT = 900
BG_COLOR = (255,255,255)
BLACK = (0, 0, 255)
SIZE = (WIDTH, HEIGHT)
SIZE2 = (WIDTH/2, HEIGHT/2)

class Character(spyral.Sprite):
    def __init__(self):
        score = 0

    # Character animations
    def setAnimations(self,scene):

        # right walk animation sequence
        right = ["game/images/Animations/b1.bmp", "game/images/Animations/b2.bmp", "game/images/Animations/b3.bmp",
        "game/images/Animations/b4.bmp","game/images/Animations/b5.bmp", "game/images/Animations/b6.bmp", 
        "game/images/Animations/b7.bmp","game/images/Animations/b8.bmp"]
        images = [spyral.Image(filename=f) for f in right]

        # left walk animation sequence
        left = ["game/images/Animations/bl1.bmp", "game/images/Animations/bl2.bmp", "game/images/Animations/bl3.bmp", 
        "game/images/Animations/bl4.bmp","game/images/Animations/bl5.bmp", "game/images/Animations/bl6.bmp", 
        "game/images/Animations/bl7.bmp","game/images/Animations/bl8.bmp"]
        images2 = [spyral.Image(filename=f) for f in left]

        #right stop animation sequence
        stop_right = ["game/images/Animations/stop2.bmp"]
        stopR = [spyral.Image(filename=f) for f in stop_right]
        #left stop animation sequence
        stop_left = ["game/images/Animations/stop2l.bmp"]
        stopL = [spyral.Image(filename=f) for f in stop_left]

        # Animation
        self.animation = Animation('image', easing.Iterate(images), duration = 1.5, loop=True)
        self.animation2 = Animation('image', easing.Iterate(images2), duration = 1.5, loop=True)
        self.stop_l = Animation('image', easing.Iterate(stopL), duration = 1.5)
        self.stop_r = Animation('image', easing.Iterate(stopR), duration = 1.5)
        

    def setScene(self,scene):
        super(Character, self).__init__(scene)

    
    def setImage(self,imagePath):
    #"game/images/stick.bmp"
        self.image = spyral.Image(filename=imagePath)
        self.anchor = "center"
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.moving = False 
        self.vel = 150
    

    def setKeyBoardCommands(self,scene):
        # Key down
        spyral.event.register("input.keyboard.down.left", self.move_left)
        spyral.event.register("input.keyboard.down.right", self.move_right)
        spyral.event.register("input.keyboard.down.down", self.move_down)
        spyral.event.register("input.keyboard.down.up", self.move_up)

        # Key up
        spyral.event.register("input.keyboard.up.left", self.stop_move)
        spyral.event.register("input.keyboard.up.right", self.stop_move)
        spyral.event.register("input.keyboard.up.down", self.stop_move)
        spyral.event.register("input.keyboard.up.up", self.stop_move)
        spyral.event.register('director.update', self.update)

    def setScene(self,scene,row,column):
        super(Character,self).__init__(scene)
        self.sceneRow = row
        self.sceneColumn = column

    def setSceneMatrix(self,matrix):
        self.sceneMatrix = matrix

    def leavingScene(self):
        row = self.sceneRow
        column = self.sceneColumn
        distance = 100
    	if(self.x < 0 and self.sceneColumn != 0):
    		spyral.director.replace(self.sceneMatrix[row][column - 1])
    		self.setScene(self.sceneMatrix[row][column - 1],row,column - 1)
    		self.sceneMatrix[row][column - 1].setCharacter(self)
    		self.setImage("game/images/Animations/stop2l.bmp")
    		self.x = WIDTH - distance
    		
    	elif(self.x > WIDTH and self.sceneColumn != 3):
    		spyral.director.replace(self.sceneMatrix[row][column + 1])
    		self.setScene(self.sceneMatrix[row][column + 1],row,column + 1)
    		self.sceneMatrix[row][column + 1].setCharacter(self)
    		self.setImage("game/images/Animations/stop2.bmp")
    		self.x = distance

    	elif(self.y < 0 and self.sceneRow != 0):
    		spyral.director.replace(self.sceneMatrix[row - 1][column])
    		self.setScene(self.sceneMatrix[row - 1][column],row - 1,column)
    		self.sceneMatrix[row - 1][column].setCharacter(self)
    		self.setImage("game/images/Animations/stop2.bmp")
    		self.y = HEIGHT - distance

    	elif(self.y > HEIGHT and self.sceneRow != 3):
    		spyral.director.replace(self.sceneMatrix[row + 1][column])
    		self.setScene(self.sceneMatrix[row + 1][column],row + 1,column)
    		self.sceneMatrix[row + 1][column].setCharacter(self)
    		self.setImage("game/images/Animations/stop2.bmp")
    		self.y = distance

    def move_left(self):
        self.moving = 'left'
        self.vel = 150
        self.stop_all_animations()
        self.animate(self.animation2)
    def move_right(self):
        self.moving = 'right'
        self.vel = 150
        self.stop_all_animations()
        self.animate(self.animation)
    def move_down(self):
        self.moving = 'down'
        self.vel = 150
    def move_up(self):
        self.moving = 'up'
        self.vel = 150
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

    def collide_item(self, item):

        if (self.collide_sprite(item)):
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

