import spyral
import Board
#import Character
#import Monster
def main():

    spyral.director.init(size=(0, 0), max_ups=30, max_fps=30, fullscreen=False, caption='The Game')
    scene_matrix = [[0 for x in xrange(5)] for x in xrange(5)]#sets up the 4x4 game board
    backGroundImage = 1
    character = Character.Character()
    monsters = []
    for l in range(10):
        temp = Monster.Monster()
        monsters.append(temp)
    
    for i in range(5):
        for j in range(5):
            gameBoard = Board.Board()
            gameBoard.setBackGround("game/sceneImages/1.bmp")
            gameBoard.setCharacter(character)
            gameBoard.setMonster(monsters)
            gameBoard.setWalls(i,j)
            scene_matrix[i][j] = gameBoard
			#once everything works uncomment these and fix images sizes
			#gameBoard.setBackGround("game/sceneImages/"+str(backGroundImage)+".jpg")
			#backGroundImage = backGroundImage + 1
    spyral.director.push(scene_matrix[0][0])
    character.setScene(scene_matrix[0][0])
    character.setImage("game/images/stick.bmp")
    for monster in monsters:
        monster.setScene(scene_matrix[0][0])
        monster.setImage("game/images/m1_30*30.bmp")

