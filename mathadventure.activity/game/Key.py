import spyral
import random

class Key(spyral.Sprite):
    def __init__(self, scene):
        super(Key, self).__init__(scene)
        self.layer = 'top'
        #self.scale = (100,15)
        self.pos = (600,450)

        #maybe make a key animation that moves the key across the scene and then dissapears?
        # we should also make some sort of key thing in the corner next to health maybe that shows a small key when
        # one is earned with spaces for two or three more?
        
    def setScene(self,scene):
        super(Key, self).__init__(scene)
        self.layer = 'top'
