import spyral
SIZE = (1200,900)
class LoadingScene(spyral.Scene):
	def __init__(self, *args, **kwargs):
			spyral.Scene.__init__(self, SIZE)
			self.background = spyral.Image(filename="game/sceneImages/loading.bmp")
