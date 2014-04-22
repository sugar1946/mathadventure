import spyral
import random
import Question

class Item(spyral.Sprite):
    def __init__(self,name):
        #super(Item, self).__init__(scene)
        question_level = "easy"
        attempts = 0
        self.name = name
        self.key = False
	'''
        if (self.name == "chest"):
            self.image = spyral.Image(filename=("game/images/chest.bmp"))
            self.image.scale((90,65))
        elif (self.name == "gem"):
            self.image = spyral.Image(filename=("game/images/gem.bmp"))
            self.image.scale((40,60))

        self.anchor = "bottomleft"
        self.x = x
        self.y = y
	'''


    def setScene(self,scene):
        super(Item, self).__init__(scene)

    
    def setImage(self,imagePath,x,y):
	self.current_image = imagePath
        self.image = spyral.Image(filename=imagePath)
        self.anchor = "bottomleft"
        self.x = x
        self.y = y
        
