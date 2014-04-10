import spyral
import random
import math
#import Board

WIDTH = 900
HEIGHT = 900
BG_COLOR = (255,255,255)
BLACK = (0, 0, 255)
SIZE = (WIDTH, HEIGHT)
SIZE2 = (WIDTH/2, HEIGHT/2)

class Character(spyral.Sprite):
    def __init__(self, scene):
	#change for commit
        super(Character, self).__init__(scene)

        x = WIDTH/2
        y = HEIGHT/2
        score = 0

        self.image = spyral.Image(filename="game/images/stick.png")
        self.anchor = "center"
        self.x = x
        self.y = y
        self.moving = False        

        # Key down
        spyral.event.register("input.keyboard.down.left", self.move_left)
        spyral.event.register("input.keyboard.down.right", self.move_right)
        spyral.event.register("input.keyboard.down.down", self.move_down)
        spyral.event.register("input.keyboard.down.up", self.move_up)

        # Key up
        spyral.event.register("input.keyboard.up.left", self.stop_move)
        spyral.event.register("input.keyboard.up.right", self.stop_move)
        spyral.event.register("input.keyboard.up.down", self.stop_move)
        spyral.event.register("input.keyboard.up.up", self.stop_move)
        spyral.event.register('director.update', self.update)

    def move_left(self):
        self.moving = 'left'
    def move_right(self):
        self.moving = 'right'
    def move_down(self):
        self.moving = 'down'
    def move_up(self):
        self.moving = 'up'
    def stop_move(self):
        self.moving = False

    def update(self, delta):
        character_velocity = 250

        if self.moving == 'left':
            self.x -= character_velocity * delta
        elif self.moving == 'right':
            self.x += character_velocity * delta
        elif self.moving == 'down':
            self.y += character_velocity * delta
        elif self.moving == 'up':
            self.y -= character_velocity * delta

class Opponent(spyral.Sprite):
    def __init__(self, scene):
        super(Opponent, self).__init__(scene)

        self.image = spyral.Image(filename="game/images/M1.png")
        self.x = 50
        self.y = 50
        self.anchor = 'center'

        spyral.event.register('director.update', self.update)
        self.reset()

    def reset(self):
        theta = random.random()*2*math.pi
        while ((theta > math.pi/4 and theta < 3*math.pi/4) or
            (theta > 5*math.pi/4 and theta < 7*math.pi/4)):
            theta = random.random()*2*math.pi

        r = 300

        self.vel_x = 100
        self.vel_y = 100
        
        self.pos  = (WIDTH/2, HEIGHT/2)

    def update(self, delta):
        self.x += delta * self.vel_x
        self.y += delta * self.vel_y

        if self.y > HEIGHT:
            self.y = HEIGHT
            self.vel_y = -self.vel_y
        elif self.y < 0:
            self.y = 0
            self.vel_y = -self.vel_y
        elif self.x > WIDTH:
            self.x = WIDTH
            self.vel_x = -self.vel_x
        elif self.x < 0:
            self.x = 0
            self.vel_x = -self.vel_x


class Main(spyral.Scene):

	def __init__(self, *args, **kwargs):
		super(Main, self).__init__(SIZE)
		#global manager
		#for x in range(0,9): #testing

		self.player = Character(self)
		#self.opponent = Opponent(self)
			
		spyral.event.register("system.quit", spyral.director.pop)
		spyral.event.register("input.keyboard.down.q", spyral.director.pop)
		#spyral.event.register("input.keyboard.down.b", spyral.director.replace(Board.Board()))
