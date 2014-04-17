import spyral
import random
import math
import PlayerSelectionScene

#UPDATE_SCENE = []
SIZE = (1200,900)
class StartScene(spyral.Scene):
	def __init__(self, *args, **kwargs):
			spyral.Scene.__init__(self, SIZE)
			self.background = spyral.Image(filename="game/sceneImages/loading.jpg")
			spyral.event.register("input.keyboard.down.q", spyral.director.pop)
			spyral.event.register("input.keyboard.down.t", spyral.director.pop)
			spyral.event.register("input.keyboard.down.s", self.startGame)


	def startGame(self):
		spyral.director.replace(PlayerSelectionScene.PlayerSelectionSceneMain())
		
