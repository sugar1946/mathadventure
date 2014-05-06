import spyral
import random
import math


WIDTH = 1200
HEIGHT = 900
BG_COLOR = (255,255,255)
BLACK = (0, 0, 255)
SIZE = (WIDTH, HEIGHT)
SIZE2 = (WIDTH/2, HEIGHT/2)
MONSTER = "game/images/m1.bmp"


class Monster(spyral.Sprite):
    def __init__(self,scene,image,x,y):
        super(Monster, self).__init__(scene)
        self.image = spyral.Image(filename=(image))
        self.score = 0
        self.anchor ='center'
        direction = random.choice(['up','down','left','right'])
        self.x = x
        self.y = y
        self.direction = direction
        self.frozen = False
        self.vel_x = 25
        self.vel_y = 25
        spyral.event.register('director.update', self.update)


    ##def setScene(self,scene):
        #super(Monster,self).__init__(scene)

   ## def setImage(self,imagePath,x,y):
    #"game/images/stick.png"
 ##       self.image = spyral.Image(filename=imagePath)
##        self.anchor = "center"
 
        
    def update(self,delta):
        if (self.frozen == False):
            if (self.direction == 'up'):
                self.y = self.y - delta * self.vel_y
            elif (self.direction == 'down'):
                self.y = self.y + delta * self.vel_y
            elif (self.direction == 'left'):
                self.x = self.x + delta * self.vel_x
            elif (self.direction == 'right'):
                self.x = self.x - delta*self.vel_x
 

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
        

    def setUpdate(self,scene):
        spyral.event.register('director.update', self.update)

    def collide_wall(self,wall):
        if self.collide_sprite(wall):
            if(self.direction == 'up' or self.direction == 'down'):
                self.vel_y = -self.vel_y
            if(self.direction == 'left' or self.direction == 'right'):
                self.vel_x = -self.vel_x
 
        
    def collide_monster(self,monster):
        if self.collide_sprite(monster):
            if(self.direction == 'up' or self.direction == 'down'):
                self.vel_y = -self.vel_y
            if(self.direction == 'left' or self.direction == 'right'):
                self.vel_x = -self.vel_x

    def collide_player(self,character):
        if self.collide_sprite(character):
            ##if(self.direction == 'up' or self.direction == 'down'):
##                self.vel_y = -self.vel_y
##            if(self.direction == 'left' or self.direction == 'right'):
##                self.vel_x = -self.vel_x
            self.kill()
            character.damage()

    

    def collide_item(self,item):
        
        if self.collide_sprite(item):
            if(item.name == 'key'):
                item.kill()
                
            else:
                if(self.direction == 'up' or self.direction == 'down'):
                     self.vel_y = -self.vel_y
                if(self.direction == 'left' or self.direction == 'right'):
                     self.vel_x = -self.vel_x
  

