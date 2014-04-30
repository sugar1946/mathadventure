import spyral
import random
import Question

class Item(spyral.Sprite):
    def __init__(self, scene, name):
        super(Item, self).__init__(scene)
        self.name = name
        self.layer = 'bottom'

    def setScene(self,scene):
        super(Item, self).__init__(scene)

    
    def setImage(self,imagePath,x,y):
        self.current_image = imagePath
        self.image = spyral.Image(filename=imagePath)
        self.anchor = "bottomleft"
        self.x = x
        self.y = y

    def setFraction(self):
        self.top_number = random.randint(1,3)
        top = Text(str(self.top_number)).getimage()
        self.image.draw_image(top, position=(12, 5))
        self.bottom_number = random.randint(4,12)
        bottom = Text(str(self.bottom_number)).getimage()
        if (self.bottom_number > 9):
            self.image.draw_image(bottom,position=(6,25) )
        elif(self.bottom_number <= 9):
            self.image.draw_image(bottom,position=(12,25) )

class Text(spyral.Image):
        def __init__(self,text):
            font = spyral.Font("libraries/spyral/resources/fonts/DejaVuSans.ttf", 20)
            self.image = font.render(text, color=(0,0,0))
            self.anchor = "bottomleft"
        def getimage(self):
            return self.image
