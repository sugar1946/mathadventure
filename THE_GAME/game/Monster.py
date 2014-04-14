import spyral
import random
import math

WIDTH = 900
HEIGHT = 900
BG_COLOR = (255,255,255)
BLACK = (0, 0, 255)
SIZE = (WIDTH, HEIGHT)
SIZE2 = (WIDTH/2, HEIGHT/2)
MONSTER = "game/images/m1.bmp"


class Monster(spyral.Sprite):
    def __init__(self):
        #super(Character, self).__init__(scene)
        score = 0
        
        

    def setScene(self,scene):
        super(Monster,self).__init__(scene)

    def setImage(self,imagePath):
    #"game/images/stick.png"
        self.image = spyral.Image(filename=imagePath)
        self.anchor = "center"
        self.x=100*random.random()
        self.y=100*random.random()
        self.moving = False
        self.vel_x = 20
        self.vel_y = 20
        
    def update(self,delta):
        self.x += delta * self.vel_x
        self.y += delta * self.vel_y
        chance = random.random();

        ## bounce
        r = self.rect
        if r.top < 30:
            r.top = 30
            self.vel_y = -self.vel_y
        if r.bottom > HEIGHT-30:
            r.bottom = HEIGHT-30
            self.vel_y = -self.vel_y
        if r.left < 30:
            r.left = 30
            self.vel_x = -self.vel_x
        if r.right > WIDTH-30:
            self.vel_x = -self.vel_x
        ##change the direction , during the move, the monster would change its direction by 30% possibility
        if(chance<=0.3):
        ## pick up a random angle for monster to move
            theta = random.random()*2*math.pi
            r = 100
            self.vel_x = r*math.cos(theta)
            self.vel_y = r*math.sin(theta)

    def setUpdate(self,scene):
        spyral.event.register('director.update', self.update)

    def collide_wall(self,wall):
        if self.collide_sprite(wall):
            self.vel_x = -self.vel_x
            self.vel_y = -self.vel_y
            self.moving = False
        
    def collide_monster(self,monster):
        if self.collide_sprite(monster):
            self.vel_x = -self.vel_x
            self.vel_y = -self.vel_y

    def collide_player(self,character):
        if self.collide_sprite(character):
           self.vel_x = -self.vel_x
           self.vel_y = -self.vel_y


