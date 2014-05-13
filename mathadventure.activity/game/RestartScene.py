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


SIZE = (1200,900)
WIDTH = 1200
HEIGHT = 900
FONT_PATH = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

class RePlayerImage(spyral.Sprite):
    def __init__(self,scene,img,side):
        spyral.Sprite.__init__(self,scene)
        self.image = spyral.Image(filename=img)
        self.y = HEIGHT/2 - 60
        if(side == 'left'):
            self.x = WIDTH/2 - 100 
        else:
            self.x = WIDTH/2 + 100

class ReSelectionMessage(spyral.Sprite):
    def __init__(self,scene,img,x,y):
        spyral.Sprite.__init__(self,scene)
        self.image = img
        self.x = x
        self.y = y                


class Main(spyral.Scene):
    def __init__(self, *args, **kwargs):
            spyral.Scene.__init__(self, SIZE)
            self.player_choice = "";
            self.background = spyral.Image(size=SIZE).fill((255,255,255))
            self.selfplayerOneImage = RePlayerImage(self,"game/images/Animations/stop2.bmp","left")
            self.selfplayerTwoImage = RePlayerImage(self,"game/images/player2.bmp","right")

            font = spyral.Font(FONT_PATH,24,(0,0,0))
            message1 = font.render("Press a Key To Select a Character:")
            self.TopMessage = ReSelectionMessage(self,message1,WIDTH/3,HEIGHT/3)
            message2 = font.render("(<--)")
            self.LeftMessage = ReSelectionMessage(self,message2,self.selfplayerOneImage.x,self.selfplayerOneImage.y + 160)
            message3 = font.render("(-->)")
            self.RightMessage = ReSelectionMessage(self,message3,self.selfplayerTwoImage.x,self.selfplayerTwoImage.y + 160)

            spyral.event.register("input.keyboard.down.q", spyral.director.pop)
            spyral.event.register("input.keyboard.down.s", self.startGame)
            spyral.event.register("input.keyboard.down.left", self.chosePlayerOne)
            spyral.event.register("input.keyboard.down.right", self.chosePlayerTwo)

    def chosePlayerOne(self):
        self.player_choice = "game/images/Animations/stop2.bmp"
        self.startGame()

    def chosePlayerTwo(self):
        self.player_choice = "game/images/player2.bmp"
        self.startGame()

    def setCharacter(self,character):
	self.character = character
    
    def resetCharacter(self):
	self.character.reset()

    def startGame(self):
        if (self.player_choice == "game/images/Animations/stop2.bmp"):
		for i in range(4):
		     for j in range(4):
			for x in (self.character.sceneMatrix[i][j].ENEMY_LIST):
				x.setImage("game/images/m1_30_30.bmp")
	else:
		for i in range(4):
		     for j in range(4):
			for x in (self.character.sceneMatrix[i][j].ENEMY_LIST):
				x.setImage("game/images/m2_30_30.bmp")
        
	spyral.director.replace(self.character.sceneMatrix[3][0])
	self.resetCharacter()
        self.character.setScene(self.character.sceneMatrix[3][0],3,0)

        self.character.setStopImage("game/images/Animations/Boy/8.png")
        self.character.setImage(self.player_choice)

