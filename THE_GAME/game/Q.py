import spyral
import random

class Question(spyral.Sprite):
    def __init__(self, scene):
        super(Question, self).__init__(scene)
        
        self.image = spyral.Image(filename=('game/images/question.png'))
        self.pos = (350,50)
        self.layer = 'top'
        #self.getDifficulty()

        #question lists
        self.ChestEasyList = [["easy question 1?", "wrong answer 1", "Wrong answer 2", "Right answer", "Right answer", 'n'],["easy question 2?", "Right answer", "Wrong answer", "wrong answer", "Right answer", 'n']]
        self.ChestMediumList = [["medium question 1?", "wrong answer", "Wrong answer", "Right answer", "Right answer", 'n'],["medium question 2?", "Right answer", "Wrong answer", "wrong answer", "Right answer", 'n']]
        self.ChestHardList = [["hard question 1?", "wrong answer", "Wrong answer", "Right answer", "Right answer", 'n'],["hard question 2?", "Right answer", "Wrong answer", "wrong answer", "Right", 'n']]

        #events
        spyral.event.register("input.keyboard.down.a", self.checkAnswerA)
        spyral.event.register("input.keyboard.down.b", self.checkAnswerB)
        spyral.event.register("input.keyboard.down.c", self.checkAnswerC)
        spyral.event.register("input.keyboard.down.x", self.returnScene)

        spyral.event.register("input.keyboard.down.e", self.easyClicked)
        spyral.event.register("input.keyboard.down.m", self.mediumClicked)
        spyral.event.register("input.keyboard.down.h", self.hardClicked)
        
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
        spyral.event.register("system.quit", spyral.director.pop)
                            

    def easyClicked(self):
        self.current_question = self.ChestEasyList[random.randint(0,len(self.ChestEasyList)-1)]
        self.current_difficultyPoints = 10
        self.setNewQuestion()


    def mediumClicked(self):
        self.current_question = self.ChestMediumList[random.randint(0,len(self.ChestMediumList)-1)]
        self.current_difficultyPoints = 20
        self.setNewQuestion()

    def hardClicked(self):
        self.current_question = self.ChestHardList[random.randint(0,len(self.ChestHardList)-1)]
        self.current_difficultyPoints = 30
        self.setNewQuestion()

        
    def setNewQuestion(self):
        self.image = spyral.Image(filename=('game/images/blank_question.png'))
        #question and answers
        question_text = QuestionText(self.current_question[0], 30).getImage()
        self.image.draw_image(question_text, position = (50,200))

        a = "A) " + str(self.current_question[1])
        a_text = QuestionText(a, 20).getImage()
        self.image.draw_image(a_text, position = (75,250))

        b = "B) "+ str(self.current_question[2])
        b_text = QuestionText(b, 20).getImage()
        self.image.draw_image(b_text, position = (75,300))

        c = "C) "+ str(self.current_question[3])
        c_text = QuestionText(c, 20).getImage()
        self.image.draw_image(c_text, position = (75,350))
        
    def checkAnswerA(self):
        if  (self.current_question[1] == self.current_question[4]):
            self.setResponseText(True)
        else:
            self.setResponseText(False)
            
    def checkAnswerB(self):
        if  (self.current_question[2] == self.current_question[4]):
            self.setResponseText(True)
        else:
            self.setResponseText(False)
            
        
    def checkAnswerC(self):
        if  (self.current_question[3] == self.current_question[4]):
            self.setResponseText(True)
        else:
            self.setResponseText(False)

    def setResponseText(self, correct):
        self.image = spyral.Image(filename=('game/images/feedback.png'))
        if (correct):
            answer_text = QuestionText("Congratulations!", 30).getImage()
            sub_text = QuestionText( " you earned " + str(self.current_difficultyPoints) + " points!", 25).getImage()
        else:
            answer_text = QuestionText("I'm Sorry", 30).getImage()
            sub_text = QuestionText("The correct answer is " + str(self.current_question[4]) , 25).getImage()
        self.image.draw_image(answer_text, position = (100,100))
        self.image.draw_image(sub_text, position = (75,150))

    def returnScene(self):
        self.kill()

        
class QuestionText(spyral.Image):
    def __init__(self, text, size):
        font = spyral.Font("libraries/spyral/resources/fonts/DejaVuSans.ttf", size)
        self.image = font.render(text, color=(0,0,0))
    def getImage(self):
        return self.image


        



         
