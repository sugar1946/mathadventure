import spyral

class Scene(spyral.Sprite):
	def __init__(self, scene,side):
		spyral.Sprite.__init__(self, scene)
		self.image = spyral.Image(size=(100,100)).fill((0,0,0))
		self.x = 50
		self.y = HEIGHT * .66
