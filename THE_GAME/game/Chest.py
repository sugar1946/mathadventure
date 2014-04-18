import spyral
import random
#import Question

class Item(spyral.Sprite):
    def __init__(self, scene, name, x, y):
        super(Item, self).__init__(scene)
        question_level = "easy"
        attempts = 0
        if (name == "chest"):
            self.image = spyral.Image(filename=("game/images/chest.bmp"))
        elif (name == "gem"):
            self.image = spyral.Image(filename=("game/images/gem.bmp"))
        self.image.scale((50,80))
        self.anchor = "bottomright"
        self.x = x
        self.y = y
        
            
        
