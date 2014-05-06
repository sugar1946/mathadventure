import spyral
import PlayerSelectionScene
SIZE = (1200,900)
class Tutorial(spyral.Scene):
	def __init__(self, *args, **kwargs):
			spyral.Scene.__init__(self, SIZE)
			image = spyral.Image(filename="game/images/tutorial.png")
			image.scale((1200,900))
			self.background = image
			spyral.event.register("input.keyboard.down.q", spyral.director.pop)
			spyral.event.register("input.keyboard.down.s", self.startGame)
	def startGame(self):
		spyral.director.replace(PlayerSelectionScene.PlayerSelectionSceneMain())

		
