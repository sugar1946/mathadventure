import spyral
import Item
import random

class Question(spyral.Scene):
    def __init__(self):
        super(Question, self).__init__((1200,900))

        self.background = spyral.Image(size = (1200,900)).fill((255,255,255))

        self.GemList = [["1+2 = ", "1","2","3", "3", "n"], ["2+2 = ", "2", "4", "6", "4", "n"]]
        self.ChestEasyList = [["easy question 1", "wrong", "Wrong", "Right", "Right", 'n'],["easy question 2", "Right", "Wrong", "wrong", "Right", 'n']]
        self.ChestMediumList = [["medium question 1", "wrong", "Wrong", "Right", "Right", 'n'],["medium question 2", "Right", "Wrong", "wrong", "Right", 'n']]
        self.ChestHardList = [["hard question 1", "wrong", "Wrong", "Right", "Right", 'n'],["hard question 2", "Right", "Wrong", "wrong", "Right", 'n']]

        self.gemsRight = 0
        self.question_level = "easy"

        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
        spyral.event.register("system.quit", spyral.director.pop)

    def questionpopup(self, item):
        if (item.name == "gem"):
            popup = QuestionText(self, self.GemList[random.randint(0,len(self.GemList)-1)][0])
            popup.anchor = "topleft"
            popup.visible = True
            return True
        elif (item.name == "chest"):
            print "chest"
            return False
    

class QuestionText(spyral.Sprite):
    def __init__(self, scene, text):
        super(QuestionText, self).__init__(scene)
        font = spyral.Font("libraries/spyral/resources/fonts/DejaVuSans.ttf", 50)
        self.image = font.render(text, color=(0,0,0))
        self.anchor = "topleft"

class QuestionForm(spyral.Form):
    buttonY = spyral.widgets.Button("yes")
    buttonN = spyral.widgets.Button("no")
    text = spyral.widgets.TextInput(75)
    num = 1

         
