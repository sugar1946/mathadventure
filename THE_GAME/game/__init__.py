import spyral
import Board
import LoadingScene
#import Character
#import Monster
def main():

    spyral.director.init(size=(0, 0), max_ups=30, max_fps=30, fullscreen=False, caption='The Game')
    scene_matrix = [[0 for x in xrange(4)] for x in xrange(4)]#sets up the 4x4 game board
    backGroundImage = 1
    character = Character.Character()
    monsters = []

    for l in range(4):
        temp = Monster.Monster()
        monsters.append(temp)
    for i in range(4):
        for j in range(4):
            gameBoard = Board.Board()
			#if(j == 1):
			#	gameBoard.setBackGround("game/sceneImages/2.jpg")
			#else:

            gameBoard.setMonster(monsters)
            gameBoard.setBackGround("game/sceneImages/1_1200*900.bmp")

            gameBoard.setCharacter(character)
            gameBoard.setChestsandGems()
            gameBoard.setWalls(i,j)
            scene_matrix[i][j] = gameBoard
			#once everything works uncomment these and fix images sizes
			#gameBoard.setBackGround("game/sceneImages/"+str(backGroundImage)+".jpg")
			#backGroundImage = backGroundImage + 1
    spyral.director.push(scene_matrix[0][0])
    character.setScene(scene_matrix[0][0],0,0)
    character.setSceneMatrix(scene_matrix)
    character.setImage("game/images/stick.bmp")
    for monster in monsters:
        monster.setScene(scene_matrix[0][0])
        monster.setImage("game/images/m1_30*30.bmp")
 

