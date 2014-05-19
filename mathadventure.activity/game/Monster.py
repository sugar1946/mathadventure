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
    def __init__(self,scene):
        super(Monster, self).__init__(scene)
        #self.image = spyral.Image(filename=(image))
        self.score = 0
        self.anchor ='center'
        direction = random.choice(['up','down','left','right'])
        #self.x = x
        #self.y = y
        self.direction = direction
        self.frozen = False
        self.vel_x = 25
        self.vel_y = 25
 #       spyral.event.register('director.update', self.update)


    ##def setScene(self,scene):
        #super(Monster,self).__init__(scene)

    def setImage(self,image,x,y):
        self.image = spyral.Image(filename=image)
        self.x = x
        self.y = y

    def update(self,delta):
 
        if (self.frozen == False):
            '''if (self.x < 100):
                self.x = 100
                self.direction = 'right'
            if (self.x > WIDTH-100):
                self.x = WIDTH-100
                self.direction = 'left'
            if (self.y < 100):
                self.y = 100
                self.direction ='up'
            if (self.y > HEIGHT - 100):
                self.y = HEIGHT - 100
                self.y = 'down' '''
            if (self.direction == 'up'):
                self.y = self.y - delta * self.vel_y
            elif (self.direction == 'down'):
                self.y = self.y + delta * self.vel_y
            elif (self.direction == 'left'):
                self.x = self.x - delta * self.vel_x
            elif (self.direction == 'right'):
                self.x = self.x + delta * self.vel_x
        self.collide_wall()
 

        
        

    def setUpdate(self,scene):
        spyral.event.register('director.update', self.update)

    
    def collide_wall(self):
        ##print "collide_wall"
        ##if (self.collide_sprite(wall)):
            if ((self.y - self.height/2) < 40):
 
                self.y = 60+self.height/2
                self.direction = 'left'

            elif  ((self.y + self.height/2) > HEIGHT-40):
                self.direction = 'right'
                self.y = HEIGHT-100-self.height/2

            elif ((self.x + self.width/2) > WIDTH-40):
                 self.direction = 'up'
                 self.x = WIDTH-100-self.width/2

            elif ((self.x - self.width/2) < 40):
                 self.direction = 'down'
                 self.x = 60 + self.width/2

        
        
    def collide_monster(self,monster):
            ##print "collide_monster"
        if self.collide_sprite(monster):
            org = '?'
            if(self.direction == 'up'):
                    org = 'up'
                    self.direction = 'down'
                    self.y = self.y + 2.5
                    
                        
            elif(self.direction == 'down'):
                    org = 'down'
                    self.direction = 'up'
                    self.y = self.y-2.5
                    
            elif(self.direction == 'right'):
                    org = 'right'
                    self.direction = 'left'
                    self.x = self.x-2.5
                    
            elif(self.direction == 'left'):
                    org = 'left'
                    self.direction = 'right'
                    self.x = self.x +2.5

            if(monster.x-self.width<self.x<monster.x+monster.width)and(monster.y-monster.height<self.y<monster.y+monster.height):
                if (org !='?'):
                    self.direction = org

              
               

                
                    
          
         

    def collide_player(self,character):
        if self.collide_sprite(character):
            ##if(self.direction == 'up' or self.direction == 'down'):
##                self.vel_y = -self.vel_y
##            if(self.direction == 'left' or self.direction == 'right'):
##                self.vel_x = -self.vel_x
##            self.scene.ENEMY_LIST.remove(self)
            ##if (self.scene.EnemyNum>0):
            #self.kill()
            character.damage()
            return True          
        else:
            return False
    

    def collide_item(self,item):
            ##print "item width %d, item height %d"% (item.width,item.height)
        if(self.collide_sprite(item)):
            #print "collide happened collide_item"
            org ='?'

            if(item.name == 'key'):
                item.kill()

            

            else:                  
                if(self.direction == 'up'):
                    self.direction = 'down'
                    org ='up'
                    self.y = self.y+3
                elif(self.direction == 'down'):
                    org ='down'
                    self.direction = 'up'
                    self.y = self.y -3
                elif(self.direction == 'right'):
                    org ='right'
                    self.direction = 'left'
                    self.x = self.x-3
                elif(self.direction == 'left'):
                    org ='left'
                    self.direction = 'right'
                    self.x = self.x +3

                if(item.x-self.width/2<self.x<item.x+item.width+self.width/2)and(item.y-item.height-self.height/2<self.y<item.y+self.height/2):
                    if(org!='?'):
                        self.direction = org


  

