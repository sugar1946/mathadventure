import spyral
import Item
import random

class Question(spyral.Scene):
    def __init__(self):
        super(Question, self).__init__((1200,900))

        self.background = spyral.Image(size = (1200,900)).fill((255,255,255))
        self.return_scene = self
        self.current_question =   ["","","","","",""]
        self.gemsRight = 0
        self.question_level = "easy"
        
        #question lists
        self.GemList = [["1+2 = ", "1","2","3", "3", "n"], ["2+2 = ", "2", "4", "6", "4", "n"]]
        self.ChestEasyList = [["easy question 1", "wrong", "Wrong", "Right", "Right", 'n'],["easy question 2", "Right", "Wrong", "wrong", "Right", 'n']]
        self.ChestMediumList = [["medium question 1", "wrong", "Wrong", "Right", "Right", 'n'],["medium question 2", "Right", "Wrong", "wrong", "Right", 'n']]
        self.ChestHardList = [["hard question 1", "wrong", "Wrong", "Right", "Right", 'n'],["hard question 2", "Right", "Wrong", "wrong", "Right", 'n']]

        self.a_text = QuestionText(self, self.current_question[1])
        self.b_text = QuestionText(self, self.current_question[2])
        self.c_text = QuestionText(self, self.current_question[3])
        self.question_text = QuestionText(self, self.current_question[0])
        
        spyral.event.register("form.QuestionForm.buttonA.clicked", self.checkAnswerA)
        spyral.event.register("form.QuestionForm.buttonB.clicked", self.checkAnswerB)
        spyral.event.register("form.QuestionForm.buttonC.clicked", self.checkAnswerC)
        spyral.event.register("form.QuestionForm.buttonReturn.clicked", self.returnScene)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
        spyral.event.register("system.quit", spyral.director.pop)

    def setNewQuestion(self, item):
        if (item.name == "gem"):
            self.current_question = self.GemList[random.randint(0,len(self.GemList)-1)]
        elif (item.name == "chest"):
            self.current_question = self.ChestEasyList[random.randint(0,len(self.ChestEasyList)-1)]

        #question
        self.question_text = QuestionText(self, self.current_question[0])
        self.question_text.anchor = "topleft"
        
        #Answer text option A
        self.a_text = QuestionText(self, self.current_question[1])
        self.a_text.pos = (450, 300)
        self.a_text.anchor = "midleft"
        #Answer text option B
        self.b_text = QuestionText(self, self.current_question[2])
        self.b_text.pos = (450, 400)
        self.b_text.anchor = "midleft"
        #Answer text option C
        self.c_text = QuestionText(self, self.current_question[3])
        self.c_text.pos = (450, 500)
        self.c_text.anchor = "midleft"

        #buttons
        self.question_form = QuestionForm(self)
        self.question_form.buttonA.pos = (400, 300)
        self.question_form.buttonB.pos = (400, 400)
        self.question_form.buttonC.pos = (400, 500)
        self.question_form.buttonReturn.pos = (600, 600)
        spyral.director.replace(self)
        return
    
    def setScene(self, prev_scene):
        self.return_scene = prev_scene
    
    def setCharacter(self, character):
        self.player = character
        
    def checkAnswerA(self):
        if  (self.current_question[1] == self.current_question[4]):
            print "yes"
            self.returnScene()
        else:
            print "no"
            
    def checkAnswerB(self):
        if  (self.current_question[2] == self.current_question[4]):
            print "yes"
            self.returnScene()

        else:
            print "no"
            
    def checkAnswerC(self):
        if  (self.current_question[3] == self.current_question[4]):
            print "yes"
            self.returnScene()
        else:
            print "no"
            
    def returnScene(self):
        self.question_text.kill()
        self.a_text.kill()
        self.b_text.kill()
        self.c_text.kill()                      
        spyral.director.replace(self.return_scene)
        print "return"
        return
        
class QuestionText(spyral.Sprite):
    def __init__(self, scene, text):
        super(QuestionText, self).__init__(scene)
        font = spyral.Font("libraries/spyral/resources/fonts/DejaVuSans.ttf", 50)
        self.image = font.render(text, color=(0,0,0))
        
class QuestionForm(spyral.Form):
    buttonA = spyral.widgets.Button("A")
    buttonB = spyral.widgets.Button("B")
    buttonC = spyral.widgets.Button("C")
    buttonReturn = spyral.widgets.Button("Return")

         
