import spyral
import random
import math

WIDTH = 1200
HEIGHT = 900
BLACK = (0,0,0)
class Walls(spyral.Sprite):
	def __init__(self, scene):
        	spyral.Sprite.__init__(self, scene)
	
	def wallTopFull(self):
		self.image = spyral.Image(size=(WIDTH, 30)).fill(BLACK)

	def wallTopHalf(self,side):
		self.image = spyral.Image(size=((WIDTH/2) - 60, 30)).fill(BLACK)
		if(side == 'Right'):
			self.x = (WIDTH/2) + 60

	def wallBottomFull(self):	
		self.image = spyral.Image(size=(WIDTH, 30)).fill(BLACK)
		self.y = HEIGHT - 30

	def wallBottomHalf(self,side):	
		self.image = spyral.Image(size=((WIDTH/2) - 60, 30)).fill(BLACK)
		self.y = HEIGHT - 30
		if(side == 'Right'):
			self.x = (WIDTH/2) + 60
	
	def wallLeftFull(self):	
		self.image = spyral.Image(size=(30, HEIGHT)).fill(BLACK)

	def wallLeftHalf(self,side):	
		self.image = spyral.Image(size=(30, (HEIGHT/2) - 80)).fill(BLACK)
		if(side == 'Bottom'):
			self.y = (HEIGHT/2) + 80
	
	def wallRightFull(self):	
		self.image = spyral.Image(size=(30, HEIGHT)).fill(BLACK)
		self.x = WIDTH - 30

	def wallRightHalf(self,side):	
		self.image = spyral.Image(size=(30, (HEIGHT/2) - 80)).fill(BLACK)
		self.x = WIDTH - 30
		if(side == 'Bottom'):
			self.y = self.y = (HEIGHT/2) + 80

	def getText(self):
		return "got herre"

	
	

	

