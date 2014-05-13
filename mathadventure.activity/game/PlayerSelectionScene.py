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

class PlayerImage(spyral.Sprite):
    def __init__(self,scene,img,side):
        spyral.Sprite.__init__(self,scene)
        self.image = spyral.Image(filename=img)
        self.y = HEIGHT/2 - 120
        if(side == 'left'):
            self.x = WIDTH/2 - 200 
        else:
            self.x = WIDTH/2 + 150

class SelectionMessage(spyral.Sprite):
    def __init__(self,scene,img,x,y):
        spyral.Sprite.__init__(self,scene)
        self.image = img
        self.x = x
        self.y = y       

class Selector(spyral.Sprite):
    def __init__(self,scene):
        spyral.Sprite.__init__(self, scene)
        self.image = spyral.Image(filename="game/sceneImages/Selector.png")
        self.anchor = 'topleft'
        self.x = WIDTH/2 - 210
        self.y = self.y = HEIGHT/2 - 120
        self.pick = "left"
    animation_array = []

    def right(self):
        self.x = WIDTH/2 + 143
        self.pick = "right"
        animation_array = ["game/images/Animations/Girl/downanimation.txt","game/images/Animations/Girl/1.png"]
        self.stop
        self.animate(self.animation)

    def left(self):
        self.x = WIDTH/2 - 210
        self.pick = "left"
        animation_array = ["game/images/Animations/Boy/downanimation.txt","game/images/Animations/Boy/1.png"]
        self.stop
        self.animate(self.animation)

    if (animation_array != None):
        down = self.setAnimationArray(animation_array[0])
        images = [spyral.Image(filename=f) for f in down]
        #up stop animation sequence
        stop = [spyral.Image(filename=animation_array[1])]
        self.animation = Animation('image', easing.Iterate(images), duration = 1, loop=True)
        self.stop = Animation('image', easing.Iterate(stop), duration = 1)


class PlayerSelectionSceneMain(spyral.Scene):
    def __init__(self, *args, **kwargs):
            spyral.Scene.__init__(self, SIZE)
            self.player_choice = "";

            self.background = spyral.Image(filename="game/sceneImages/start1.png")
            #self.background = spyral.Image(size=SIZE).fill((255,255,255))

            self.selfplayerOneImage = PlayerImage(self,"game/images/Animations/Boy/1.png","left")
            self.selfplayerTwoImage = PlayerImage(self,"game/images/Animations/Girl/1.png","right")

            font = spyral.Font(FONT_PATH,24,(0,0,0))
            message1 = font.render("Select a Character:")
            self.TopMessage = SelectionMessage(self,message1,WIDTH/3 + 100,HEIGHT/3 - 100)
            message2 = font.render("(<--)")
            self.LeftMessage = SelectionMessage(self,message2,self.selfplayerOneImage.x,self.selfplayerOneImage.y + 160)
            message3 = font.render("(-->)")
            self.RightMessage = SelectionMessage(self,message3,self.selfplayerTwoImage.x,self.selfplayerTwoImage.y + 160)
            self.selector = Selector(self)

            spyral.event.register("input.keyboard.down.q", spyral.director.pop)
            spyral.event.register("input.keyboard.down.s", self.startGame)
            spyral.event.register("input.keyboard.down.left", self.selector.left)
            spyral.event.register("input.keyboard.down.right", self.selector.right)


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
                    
                else:
                    gameBoard.setchestsandgems()
                    if (self.player_choice == "game/images/Animations/Boy/1.png"):
                        gameBoard.setMonster("game/images/m1_30_30.bmp")
                    
                    else:
                        gameBoard.setMonster("game/images/m2_30_30.bmp")
                        #print (len(gameBoard.ENEMY_LIST))
                        
                gameBoard.setBackGround("game/sceneImages/14_12_9.bmp")

                #character.ani_array = ["game/images/Animations/Boy/rightanimation.txt","game/images/Animations/Boy/9.png","game/images/Animations/Boy/leftanimation.txt","game/images/Animations/Boy/5.png","game/images/Animations/Boy/upanimation.txt","game/images/Animations/Boy/13.png","game/images/Animations/Boy/downanimation.txt","game/images/Animations/Boy/1.png"]

                if(self.player_choice == "game/images/Animations/Boy/1.png"):
                    character.ani_array = ["game/images/Animations/Boy/rightanimation.txt","game/images/Animations/Boy/8.png","game/images/Animations/Boy/leftanimation.txt","game/images/Animations/Boy/4.png","game/images/Animations/Boy/upanimation.txt","game/images/Animations/Boy/12.png","game/images/Animations/Boy/downanimation.txt","game/images/Animations/Boy/0.png"]
                else:
                    character.ani_array = ["game/images/Animations/Girl/rightanimation.txt","game/images/Animations/Girl/8.png","game/images/Animations/Girl/leftanimation.txt","game/images/Animations/Girl/4.png","game/images/Animations/Girl/upanimation.txt","game/images/Animations/Girl/12.png","game/images/Animations/Girl/downanimation.txt","game/images/Animations/Girl/0.png"]

                gameBoard.setCharacter(character,character.ani_array)

                #gameBoard.setDoor(i, j)

                gameBoard.setRestartButton()
                gameBoard.setStoreButton()
                gameBoard.setWalls(i,j)
                scene_matrix[i][j] = gameBoard

                #once everything works uncomment these and fix images sizes
                #gameBoard.setBackGround("game/sceneImages/"+str(backGroundImage)+".jpg")
                #backGroundImage = backGroundImage + 1
        spyral.director.replace(scene_matrix[3][0])
        character.setScene(scene_matrix[3][0],3,0)
        character.setSceneMatrix(scene_matrix)

        #character.setStopImage(character.ani_array)

        character.setStopImage(self.player_choice)

        character.setImage(self.player_choice)

