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
    def __init__(self,scene):
        super(Monster, self).__init__(scene)
        self.image = spyral.Image(filename=("game/images/m1_30_30.bmp"))
        self.score = 0
        self.anchor = "center"
        self.x=1200*random.random()
        self.y=900*random.random()
        self.moving = False
        self.vel_x = 15
        self.vel_y = 15
        spyral.event.register('director.update', self.update)


    def setScene(self,scene):
        super(Monster,self).__init__(scene)

    def setImage(self,imagePath):
    #"game/images/stick.png"
        self.image = spyral.Image(filename=imagePath)
        
        
    def update(self,delta):
        self.x += delta * self.vel_x
        self.y += delta * self.vel_y
        chance = random.random();

        ## bounce
        r = self.rect
        if r.top < 50:
            r.top = 50
            self.vel_y = -self.vel_y
        if r.bottom > HEIGHT-50:
            r.bottom = HEIGHT-50
            self.vel_y = -self.vel_y
        if r.left < 50:
            r.left = 50
            self.vel_x = -self.vel_x
        if r.right > WIDTH-50:
            self.vel_x = -self.vel_x
        ##change the direction , during the move, the monster would change its direction by 30% possibility
        if(chance<=0.03):
        ## pick up a random angle for monster to move
            theta = random.random()*2*math.pi
            r = 60
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
           character.damage()

    def collide_item(self,item):
        if self.collide_sprite(item):
            self.vel_x = -self.vel_x
            self.vel_y = -self.vel_y
            self.score = self.score + 1

