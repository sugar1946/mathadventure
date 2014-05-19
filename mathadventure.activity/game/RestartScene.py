import spyral
import random
import math
import Walls
import Character
import Monster
import Item
import Question
import Board
import Door
from spyral import Animation, easing


SIZE = (1200,900)
WIDTH = 1200
HEIGHT = 900
FONT_PATH = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

class RePlayerImage(spyral.Sprite):
	def __init__(self,scene,img,side):
		spyral.Sprite.__init__(self,scene)
		self.image = spyral.Image(filename=img)
		self.y = HEIGHT/2 - 120
		if(side == 'left'):
			self.x = WIDTH/2 - 200 
		else:
			self.x = WIDTH/2 + 150

class ReSelectionMessage(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = img
		self.x = x
		self.y = y                

class AnimateSprite(spyral.Sprite):
    def __init__(self,scene):
        spyral.Sprite.__init__(self, scene)
        self.image = spyral.Image(filename="game/sceneImages/Selector.png")
        self.y = -200

    def right(self):
        self.x = WIDTH/2 + 150
        self.y = HEIGHT/2 - 120
        animation_array = ["game/images/Animations/Girl/downanimation.txt","game/images/Animations/Girl/1.png"]
        self.setAnimation(animation_array)
        self.stop_all_animations()
        self.animate(self.animation)
        

    def left(self):
        self.x = WIDTH/2 - 200 
        self.y = HEIGHT/2 - 120
        animation_array = ["game/images/Animations/Boy/downanimation.txt","game/images/Animations/Boy/1.png"]
        self.setAnimation(animation_array)
        self.stop_all_animations()
        self.animate(self.animation)

    def setAnimation(self, animation_array):
        if (animation_array != None):
            character = Character.Character()

            down = character.setAnimationArray(animation_array[0])
            images = [spyral.Image(filename=f) for f in down]
            #up animation sequence
            self.animation = Animation('image', easing.Iterate(images), duration = 1, loop=True)

class Selector(spyral.Sprite):
    def __init__(self,scene):
        spyral.Sprite.__init__(self, scene)
        self.image = spyral.Image(filename="game/sceneImages/Selector.png")
        self.anchor = 'topleft'
        self.x = WIDTH/2 - 207
        self.y = HEIGHT/2 - 128
        self.pick = "left"
        self.selection = AnimateSprite(scene)

    def right(self):
        self.x = WIDTH/2 + 141.5
        self.pick = "right"
        self.selection.right()

    def left(self):
        self.x = WIDTH/2 - 208
        self.pick = "left"
        self.selection.left()

    def select(self):
        animation_array = "game/sceneImages/Selection.txt"
        self.setAnimation(animation_array)

        if (self.pick == "left"):
            self.x = WIDTH/2 - 210
            self.stop_all_animations()
            self.animate(self.animation)

        elif (self.pick == "right"):
            self.x = WIDTH/2 + 143
            self.stop_all_animations()
            self.animate(self.animation)

    def setAnimation(self, animation_array):
        if (animation_array != None):
            character = Character.Character()

            selection = character.setAnimationArray(animation_array)
            images = [spyral.Image(filename=f) for f in selection]
            #up animation sequence
            self.animation = Animation('image', easing.Iterate(images), duration = 0.9)

class Main(spyral.Scene):
	def __init__(self, *args, **kwargs):
		spyral.Scene.__init__(self, SIZE)
		self.player_choice = "";
		self.background = spyral.Image(filename="game/sceneImages/start1.png")
		font = spyral.Font(FONT_PATH,24,(0,0,0))
		message1 = font.render("Press a Key To Select a Character:")
		self.TopMessage = ReSelectionMessage(self,message1,WIDTH/3,HEIGHT/3)
		self.selector = Selector(self)
		self.selfplayerOneImage = RePlayerImage(self,"game/images/Animations/Boy/1.png","left")
		self.selfplayerTwoImage = RePlayerImage(self,"game/images/Animations/Girl/1.png","right")
		message2 = font.render("(<--)")
		self.LeftMessage = ReSelectionMessage(self,message2,self.selfplayerOneImage.x,self.selfplayerOneImage.y + 160)
		message3 = font.render("(-->)")
		self.RightMessage = ReSelectionMessage(self,message3,self.selfplayerTwoImage.x,self.selfplayerTwoImage.y + 160)
		spyral.event.register("input.keyboard.down.q", spyral.director.pop)
		spyral.event.register("Selector.image.animation.end", self.startGame)
		spyral.event.register("input.keyboard.down.s", self.selector.select)
		spyral.event.register("input.keyboard.down.return", self.selector.select)
		spyral.event.register("input.keyboard.down.left", self.selector.left)
		spyral.event.register("input.keyboard.down.left", self.display)
		spyral.event.register("input.keyboard.down.right", self.selector.right)
		spyral.event.register("input.keyboard.down.right", self.display)

	def display(self):
		font = spyral.Font(FONT_PATH,24,(0,0,0))
		self.selfplayerTwoImage.kill()
		self.selfplayerOneImage.kill()

		if (self.selector.pick == "right"):
			self.selfplayerOneImage = RePlayerImage(self,"game/images/Animations/Boy/1.png","left")
		
		elif (self.selector.pick == "left"):
			self.selfplayerTwoImage = RePlayerImage(self,"game/images/Animations/Girl/1.png","right")

	def chosePlayerOne(self):
		self.player_choice = "game/images/Animations/Boy/1.png"
		self.startGame()

	def chosePlayerTwo(self):
		self.player_choice = "game/images/Animations/Girl/1.png"
		self.startGame()

	def setCharacter(self,character):
		self.character = character
    
	def resetCharacter(self):
		self.character.reset()

	def startGame(self):
		if (self.selector.pick == "left"):
			self.player_choice = "game/images/Animations/Boy/1.png"
		elif (self.selector.pick == "right"):
			self.player_choice = "game/images/Animations/Girl/1.png"

		if (self.player_choice == "game/images/Animations/Boy/1.png"):
			for i in range(4):
				for j in range(4):  
                                        for enemy in self.character.sceneMatrix[i][j].ENEMY_LIST:
                                                enemy.kill()
                                        self.character.sceneMatrix[i][j].ENEMY_LIST = []
                                        for item in self.character.sceneMatrix[i][j].ITEM_LIST:
                                                item.kill()
                                        self.character.sceneMatrix[i][j].ITEM_LIST = []

                                        if (i == 0 and j ==3):
                                                self.character.sceneMatrix[i][j].setEndGems()
                                                self.character.sceneMatrix[i][j].setBoss()
                                        else:
                                                self.character.sceneMatrix[i][j].setMonster("game/images/m1_30_30.bmp")
                                                self.character.sceneMatrix[i][j].setchestsandgems()
                                        if(self.character.sceneMatrix[i][j].finalscreen != ''):
                                            self.character.sceneMatrix[i][j].finalscreen.killScene()
                                            self.character.sceneMatrix[i][j].finalscreen = ''
                                        if(self.character.sceneMatrix[i][j].winscreen != ''):
                                            self.character.sceneMatrix[i][j].winscreen.killScene()
                                            self.character.sceneMatrix[i][j].winscreen = ''

		else:
			for i in range(4):
				for j in range(4):
                                        for enemy in self.character.sceneMatrix[i][j].ENEMY_LIST:
                                                enemy.kill()
                                        self.character.sceneMatrix[i][j].ENEMY_LIST = []
                                        for item in self.character.sceneMatrix[i][j].ITEM_LIST:
                                                item.kill()
                                        self.character.sceneMatrix[i][j].ITEM_LIST = []

                                        if (i == 0 and j ==3):
                                                self.character.sceneMatrix[i][j].setEndGems()
                                                self.character.sceneMatrix[i][j].setBoss()
                                        else:
                                                self.character.sceneMatrix[i][j].setMonster("game/images/monster2.png")
                                                self.character.sceneMatrix[i][j].setchestsandgems()
                                        if(self.character.sceneMatrix[i][j].finalscreen != ''):
                                            self.character.sceneMatrix[i][j].finalscreen.killScene()
                                            self.character.sceneMatrix[i][j].finalscreen = ''
                                        if(self.character.sceneMatrix[i][j].winscreen != ''):
                                            self.character.sceneMatrix[i][j].winscreen.killScene()
                                            self.character.sceneMatrix[i][j].winscreen = ''
                spyral.director.replace(self.character.sceneMatrix[3][0])
		self.resetCharacter()
		if(self.player_choice == "game/images/Animations/Boy/1.png"):
			self.character.ani_array = ["game/images/Animations/Boy/rightanimation.txt","game/images/Animations/Boy/leftanimation.txt","game/images/Animations/Boy/upanimation.txt","game/images/Animations/Boy/downanimation.txt"]
		else:
			self.character.ani_array = ["game/images/Animations/Girl/rightanimation.txt","game/images/Animations/Girl/leftanimation.txt","game/images/Animations/Girl/upanimation.txt","game/images/Animations/Girl/downanimation.txt"]
		self.character.sceneMatrix[3][0].setCharacter(self.character,self.character.ani_array,True)
		self.character.setScene(self.character.sceneMatrix[3][0],3,0)
		self.character.setStopImage(self.character.ani_array)
		self.character.setImage(self.player_choice)
	
