import spyral
import random
#import Question

class Chest(spyral.Sprite):
    def __init__(self, scene, x, y):
        super(Chest, self).__init__(scene)
        question_level = "easy"
        attempts = 0
        
        self.image = spyral.Image(filename=("game/images/chest.bmp"))
        self.image.scale((50,80))
        self.anchor = "bottomright"
        self.x = x
        self.y = y
    
            
        
