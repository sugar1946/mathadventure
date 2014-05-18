import spyral
import random

class Item(spyral.Sprite):
    def __init__(self, scene, name):
        #super(Item, self).__init__(scene)
        self.name = name
        self.fraction = 0

    def setScene(self,scene):
        super(Item, self).__init__(scene)
        self.layer = 'bottom'
    
    def setImage(self,imagePath,x,y):
        self.current_image = imagePath
        self.image = spyral.Image(filename=imagePath)
        self.anchor = "bottomleft"
        self.x = x
        self.y = y

    def setFraction(self):
        self.top_number = random.randint(1,3)
        top = Text(str(self.top_number)).getimage()
        self.bottom_number = random.choice([4,5,6,8,9,10,12])
        bottom = Text(str(self.bottom_number)).getimage()
        self.fraction = float(self.top_number)/self.bottom_number
        
        if (self.name == "gem"):
            self.image.draw_image(top, position=(40, 25))
            if (self.bottom_number > 9):
                self.image.draw_image(bottom,position=(35,50))
            elif(self.bottom_number <= 9):
                self.image.draw_image(bottom,position=(40,50))
        elif (self.name == "End Gem"):
            self.image.draw_image(top, position=(40, 25))
            if (self.bottom_number > 9):
                self.image.draw_image(bottom,position=(35,50))
            elif(self.bottom_number <= 9):
                self.image.draw_image(bottom,position=(40,50))

        
class Text(spyral.Image):
        def __init__(self,text):
            font = spyral.Font("libraries/spyral/resources/fonts/DejaVuSans.ttf", 20)
            self.image = font.render(text, color=(0,0,0))
            self.anchor = "bottomleft"
        def getimage(self):
            return self.image
