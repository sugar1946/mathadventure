import spyral
import random
import math
WIDTH = 900
HEIGHT = 900
BG_COLOR = (255,255,255)
BLACK = (0, 0, 255)
SIZE = (WIDTH, HEIGHT)
SIZE2 = (WIDTH/2, HEIGHT/2)

class Character(spyral.Sprite):
    def __init__(self):
        #super(Character, self).__init__(scene)
	score = 0
        

    def setScene(self,scene):
	super(Character,self).__init__(scene)
	
    def setImage(self,imagePath):
	#"game/images/stick.png"
	self.image = spyral.Image(filename=imagePath)
        self.anchor = "center"
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.moving = False 
	self.vel = 250
	

    def setKeyBoardCommands(self,scene):
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

    def setScene(self,scene):
	super(Character,self).__init__(scene)

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
        if self.moving == 'left':
            self.x -= (self.vel + 1) * delta
        elif self.moving == 'right':
            self.x += self.vel * delta
        elif self.moving == 'down':
            self.y += self.vel * delta
        elif self.moving == 'up':
            self.y -= self.vel * delta

    def collide_wall(self,wall):
	if self.collide_sprite(wall):
		self.vel = -self.vel
		self.moving = False

