#Robert Jones 
#CISC 374
import spyral
import random
import math

WIDTH = 900
HEIGHT = 900
BG_COLOR = (255,255,255)
BLACK = (0, 0, 255)
SIZE = (WIDTH, HEIGHT)

class Main(spyral.Scene):

	def __init__(self, *args, **kwargs):
		global manager
		spyral.Scene.__init__(self, SIZE)
		self.background = spyral.Image(size=SIZE).fill(BG_COLOR)
		spyral.event.register("system.quit", spyral.director.pop)
		spyral.event.register("input.keyboard.down.q", spyral.director.pop)
