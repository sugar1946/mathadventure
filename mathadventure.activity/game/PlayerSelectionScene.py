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

class PlayerImage(spyral.Sprite):
    def __init__(self,scene,img,side):
        spyral.Sprite.__init__(self,scene)
        self.image = spyral.Image(filename=img)
        self.y = HEIGHT/2 - 120
        if(side == 'left'):
            self.x = WIDTH/2 - 200 
        else:
            self.x = WIDTH/2 + 150

    def hide(self):
        self.x = 0
        self.y = 0

    def show(self):
        self.x = WIDTH/2 - 200 
        self.y = WIDTH/2 + 150

class SelectionMessage(spyral.Sprite):
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

# The box for selecting a character
class Selector(spyral.Sprite):
    def __init__(self,scene):
        spyral.Sprite.__init__(self, scene)
        self.image = spyral.Image(filename="game/sceneImages/Selector.png")
        self.anchor = 'topleft'
        self.x = WIDTH/2 - 35
        self.y = HEIGHT/2 - 128
        self.pick = "None"
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

class PlayerSelectionSceneMain(spyral.Scene):
    def __init__(self, *args, **kwargs):
            spyral.Scene.__init__(self, SIZE)
            self.player_choice = "";

            self.background = spyral.Image(filename="game/sceneImages/start1.png")
            #self.background = spyral.Image(size=SIZE).fill((255,255,255))

            font = spyral.Font(FONT_PATH,24,(250,250,250))
            message1 = font.render("Select a Character:")
            self.TopMessage = SelectionMessage(self,message1,WIDTH/3 + 100,HEIGHT/3 - 100)
            self.selector = Selector(self)

            self.selfplayerOneImage = PlayerImage(self,"game/images/Animations/Boy/1.png","left")
            self.selfplayerTwoImage = PlayerImage(self,"game/images/Animations/Girl/1.png","right")
            message2 = font.render("(<--)")
            self.LeftMessage = SelectionMessage(self,message2,self.selfplayerOneImage.x,self.selfplayerOneImage.y + 150)
            message3 = font.render("(-->)")
            self.RightMessage = SelectionMessage(self,message3,self.selfplayerTwoImage.x,self.selfplayerTwoImage.y + 150)


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
            self.selfplayerOneImage = PlayerImage(self,"game/images/Animations/Boy/1.png","left")
            
        elif (self.selector.pick == "left"):
            self.selfplayerTwoImage = PlayerImage(self,"game/images/Animations/Girl/1.png","right")


    def chosePlayerOne(self):
        self.player_choice = "game/images/Animations/Boy/1.png"
        self.startGame()

    def chosePlayerTwo(self):
        self.player_choice = "game/images/Animations/Girl/1.png"
        self.startGame()

    def setReturn(self,scene):
        self.ReturnScene = scene

    def startGame(self):
        scene_matrix = [[0 for x in xrange(4)] for x in xrange(4)]#sets up the 4x4 game board
        backGroundImage = 1
        character = Character.Character()

        if (self.selector.pick == "left"):
            self.player_choice = "game/images/Animations/Boy/1.png"
            print(self.selector.pick)
        elif (self.selector.pick == "right"):
            self.player_choice = "game/images/Animations/Girl/1.png"
            print(self.selector.pick)

        #door = Door.Door()
        for i in range(4):
            for j in range(4):
                gameBoard = Board.Board()
                #if(j == 1):
                #    gameBoard.setBackGround("game/sceneImages/2.jpg")
                #else:
                if (i == 0 and j == 3):
                    gameBoard.setEndGems()
		    gameBoard.setBoss()
                    
                else:

                    gameBoard.setchestsandgems()
                    if (self.player_choice == "game/images/Animations/Boy/1.png"):

                        gameBoard.setMonster("game/images/m1_30_30.bmp")
                    
                    else:
                        gameBoard.setMonster("game/images/monster2.png")
                        #print (len(gameBoard.ENEMY_LIST))
                        
                gameBoard.setBackGround("game/sceneImages/14_12_9.bmp")

                #character.ani_array = ["game/images/Animations/Boy/rightanimation.txt","game/images/Animations/Boy/9.png","game/images/Animations/Boy/leftanimation.txt","game/images/Animations/Boy/5.png","game/images/Animations/Boy/upanimation.txt","game/images/Animations/Boy/13.png","game/images/Animations/Boy/downanimation.txt","game/images/Animations/Boy/1.png"]

                if(self.player_choice == "game/images/Animations/Boy/1.png"):
                    character.ani_array = ["game/images/Animations/Boy/rightanimation.txt","game/images/Animations/Boy/leftanimation.txt","game/images/Animations/Boy/upanimation.txt","game/images/Animations/Boy/downanimation.txt"]
                else:
                    character.ani_array = ["game/images/Animations/Girl/rightanimation.txt","game/images/Animations/Girl/leftanimation.txt","game/images/Animations/Girl/upanimation.txt","game/images/Animations/Girl/downanimation.txt"]

                # This will initialize keyboard commands in the first scene only
                self.set = False
                if (i == 3 and j == 0):
                    self.set = True
                else:
                    self.set = False
                gameBoard.setCharacter(character,character.ani_array,self.set)

                gameBoard.setDoor(i, j)

                gameBoard.setRestartButton()
		gameBoard.setQuitButton()
                gameBoard.setStoreButton()
                gameBoard.setWalls(i,j)
                scene_matrix[i][j] = gameBoard

        spyral.director.replace(scene_matrix[3][0])
        character.setScene(scene_matrix[3][0],3,0)
        character.setSceneMatrix(scene_matrix)

        character.setStopImage(character.ani_array)

        character.setImage(self.player_choice)

