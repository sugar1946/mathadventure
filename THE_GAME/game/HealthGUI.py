import spyral
import random
import math

WIDTH = 1200
HEIGHT = 900

class HealthGUI(spyral.Sprite):
    def __init__(self,scene):
        super(HealthGUI, self).__init__(scene)
        self.image = spyral.Image(size=(150, 20)).fill((100, 255, 100))
        self.anchor = "midleft"
        self.x = WIDTH - 200
        self.y = 60
        self.health = 150

    def setKeyBoardCommands(self,scene):
        # Key down
        spyral.event.register("input.keyboard.down.p", self.subten)

        # Key up
        '''spyral.event.register("input.keyboard.up.l", self.stop_move)
                                spyral.event.register('director.update', self.update)'''


    def setScene(self,scene):
        super(HealthGUI,self).__init__(scene)
            
    def setImage(self,x):
        self.image = spyral.Image(size=(x, 20)).fill((100, 255, 100))
        
    def subten(self):
        if (self.health - 10 >= 0):
            self.health-=10
            self.setImage(self.health)

    #def update(self,delta):
        #blah
    def setUpdate(self,scene):
        spyral.event.register('director.update', self.update)
