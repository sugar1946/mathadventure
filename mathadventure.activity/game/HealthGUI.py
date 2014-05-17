import spyral
import random
import math

WIDTH = 1200
HEIGHT = 900

class HealthGUI(spyral.Sprite):
    def __init__(self):
        '''self.image = spyral.Image(size=(5, 20)).fill((0, 0, 0))
                                self.anchor = "midleft"
                                self.x = WIDTH - 200
                                self.y = 60
                                self.health = 150'''

    def setScene(self,scene):
        super(HealthGUI,self).__init__(scene)
            
    def setImage(self,x):
        self.image = spyral.Image(size=(x, 20)).fill((100, 255, 100))
        self.anchor = "midleft"
        self.x = WIDTH - 200
        self.y = 60
        self.health = x

    # This initializes a health container to 
    # better display remaining health
    def setContainer(self,x):
        self.image = spyral.Image(size=(x,25))
        self.image.draw_rect((175,175,175), (0,-1), (x,25), border_width=6,)
        self.anchor = "midleft"
        self.x = WIDTH - 200
        self.y = 60

    # This is for updating health amount
    def sub(self, x):
        self.health = x
        self.setImage(x)

    def setUpdate(self,scene):
        spyral.event.register('director.update', self.update)
