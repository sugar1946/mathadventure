import spyral
import random
import math

WIDTH = 1200
HEIGHT = 900

class Door(spyral.Sprite):
    def __init__(self, scene):
        spyral.Sprite.__init__(self, scene)
        '''self.image = spyral.Image(size=(5, 20)).fill((0, 0, 0))
                                self.anchor = "midleft"
                                self.x = WIDTH - 200
                                self.y = 60
                                self.health = 150'''


    def setScene(self,scene):
        super(Door,self).__init__(scene)
            
    def setImage(self, pos):
        if (pos == "1"):
            self.image = spyral.Image(filename="game/images/door2.png")
            self.anchor = "center"
            self.x = WIDTH/2
            self.y = 18
        elif (pos == "2"):
            self.image = spyral.Image(filename="game/images/door.png")
            self.anchor = "center"
            self.x = WIDTH-18
            self.y = HEIGHT/2
        
        # This is reached, but no image is produced
        #print("testing door")

    def collide(self):
        self.kill()

    def setUpdate(self,scene):
        spyral.event.register('director.update', self.update)


    
