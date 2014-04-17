import spyral
import random
import math
import Walls
import Character
import Monster
import Item
import Question
import Board

#UPDATE_SCENE = []
SIZE = (1200,900)
class StartScene(spyral.Scene):
	def __init__(self, *args, **kwargs):
			spyral.Scene.__init__(self, SIZE)
			
			self.background = spyral.Image(filename="game/sceneImages/loading.bmp")
			spyral.event.register("input.keyboard.down.q", spyral.director.pop)
			spyral.event.register("input.keyboard.down.t", spyral.director.pop)
			spyral.event.register("input.keyboard.down.s", self.startGame)
			#spyral.event.register("director.update", self.update)

	def startGame(self):
		scene_matrix = [[0 for x in xrange(4)] for x in xrange(4)]#sets up the 4x4 game board
		backGroundImage = 1
		character = Character.Character()
	
		
		for i in range(4):
			for j in range(4):
				gameBoard = Board.Board()
				#if(j == 1):
				#	gameBoard.setBackGround("game/sceneImages/2.jpg")
				#else:

				gameBoard.setMonster()
				gameBoard.setBackGround("game/sceneImages/1_1200_900.bmp")

				gameBoard.setCharacter(character)
				gameBoard.setChestsandGems()
				gameBoard.setWalls(i,j)
				scene_matrix[i][j] = gameBoard
				#once everything works uncomment these and fix images sizes
				#gameBoard.setBackGround("game/sceneImages/"+str(backGroundImage)+".jpg")
				#backGroundImage = backGroundImage + 1
		spyral.director.replace(scene_matrix[0][0])
		character.setScene(scene_matrix[0][0],0,0)
		character.setSceneMatrix(scene_matrix)
		character.setImage("game/images/stick.bmp")
		
