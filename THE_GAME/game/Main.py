import spyral
import random
import math
import Board

WIDTH = 900
HEIGHT = 900
BG_COLOR = (255,255,255)
BLACK = (0, 0, 255)
SIZE = (WIDTH, HEIGHT)
SIZE2 = (WIDTH/2, HEIGHT/2)

class Main(spyral.Scene):

	def __init__(self, *args, **kwargs):
		#global manager
		#for x in range(0,9): #testing
			
		spyral.Scene.__init__(self, SIZE)
		spyral.event.register("system.quit", spyral.director.pop)
		spyral.event.register("input.keyboard.down.r", spyral.director.pop)
		#spyral.event.register("input.keyboard.down.b", spyral.director.replace(Board.Board()))
