import spyral
import random
import math
WIDTH = 900
HEIGHT = 900
BG_COLOR = (255,255,255)
BLACK = (0, 0, 255)
SIZE = (WIDTH, HEIGHT)
MONSTER.IMG = "game/images/m1.bmp"

class Monster(spyral.Sprite):
    def __init__(self,scene):
        self.image = spyral.Image(filename = MONSTER.IMG)
        self.anchor = "center"
        self.x = random.random()*WIDTH
        self.y = random.random()*HEIGHT
        self.moving = False
        self.vel_x  = 50
        self.vel_y = 50
        spyral.event register('director.update',self.update)

    def update(self,delta):
        self.x += delta * self.vel_x
        self.y += delta * self.vel_y
        chance = random.random();

        ## bounce
        r = self.rect            
        if r.top < 0:
            r.top = 0
            self.vel_y = -self.vel_y
        if r.bottom > HEIGHT:
            r.bottom = HEIGHT
            self.vel_y = -self.vel_y
        if r.left < 0:
            r.left = 0
            self.vel_x = -self.vel_x
        if r.right > WIDTH:
            self.vel_x = -self.vel_x
        ##change the direction , during the move, the monster would change its direction by 30% possibility
        if(chance=<0.3):
        ## pick up a random angle for monster to move
            theta = random.random()*2*math.pi
            r = 300
            self.vel_x = r*math.cos(theta)
            self.vel_y = r*math.sin(theta)

                
    
