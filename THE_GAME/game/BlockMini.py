import spyral
import random
import math

WIDTH = 1200
HEIGHT = 900

class BlockMini(spyral.Sprite):
    def __init__(self,scene,image):
        super(BlockMini, self).__init__(scene)
        self.score = 0
        self.anchor = "center"

    def setScene(self,scene):
        super(BlockMini,self).__init__(scene)

    def setImage(self,imagePath):
        
        
    def update(self,delta):


    def setUpdate(self,scene):
        spyral.event.register('director.update', self.update)

    
