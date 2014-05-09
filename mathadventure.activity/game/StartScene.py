import spyral
import PlayerSelectionScene
import Tutorial
SIZE = (1200,900)
class StartScene(spyral.Scene):
	def __init__(self, *args, **kwargs):
			spyral.Scene.__init__(self, SIZE)
			image = spyral.Image(filename="game/sceneImages/start_converted.bmp")
			image.scale((1200,900))
			self.background = image
			spyral.event.register("input.keyboard.down.q", spyral.director.pop)
			spyral.event.register("input.keyboard.down.s", self.startGame)
			spyral.event.register("input.keyboard.down.t", self.openTutorial)
	def startGame(self):
		spyral.director.replace(PlayerSelectionScene.PlayerSelectionSceneMain())

        def openTutorial(self):
                spyral.director.replace(Tutorial.Tutorial())
