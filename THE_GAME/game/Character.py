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
        character_velocity = 250

        if self.moving == 'left':
            self.x -= character_velocity * delta
        elif self.moving == 'right':
            self.x += character_velocity * delta
        elif self.moving == 'down':
            self.y += character_velocity * delta
        elif self.moving == 'up':
            self.y -= character_velocity * delta
