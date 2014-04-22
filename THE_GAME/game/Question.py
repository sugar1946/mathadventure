import spyral
import Item
import random

class Question(spyral.Scene):
    def __init__(self):
        super(Question, self).__init__((1200,900))

        self.background = spyral.Image(size = (1200,900)).fill((255,255,255))

        self.return_scene = self
        self.current_question = ["", "","","", "", ""]
        self.textList = []
        self.current_difficultyPoints = 0
        
        #question lists
        self.GemList = [["1+2 = ", "1","2","3", "3", "n"], ["2+2 = ", "2", "4", "6", "4", "n"]]
        self.ChestEasyList = [["easy question 1?", "wrong answer 1", "Wrong answer 2", "Right answer", "Right answer", 'n'],["easy question 2?", "Right answer", "Wrong answer", "wrong answer", "Right answer", 'n']]
        self.ChestMediumList = [["medium question 1?", "wrong answer", "Wrong answer", "Right answer", "Right answer", 'n'],["medium question 2?", "Right answer", "Wrong answer", "wrong answer", "Right answer", 'n']]
        self.ChestHardList = [["hard question 1?", "wrong answer", "Wrong answer", "Right answer", "Right answer", 'n'],["hard question 2?", "Right answer", "Wrong answer", "wrong answer", "Right", 'n']]

        
        spyral.event.register("form.QuestionForm.buttonA.clicked", self.checkAnswerA)
        spyral.event.register("form.QuestionForm.buttonB.clicked", self.checkAnswerB)
        spyral.event.register("form.QuestionForm.buttonC.clicked", self.checkAnswerC)
        spyral.event.register("form.FinishForm.finish.clicked", self.returnScene)

        spyral.event.register("form.DifficultyForm.easy.clicked", self.easyClicked)
        spyral.event.register("form.DifficultyForm.medium.clicked", self.mediumClicked)
        spyral.event.register("form.DifficultyForm.hard.clicked", self.hardClicked)
        
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
        spyral.event.register("system.quit", spyral.director.pop)

    def openQuestion(self, item):
        spyral.director.replace(self)
        self.getDifficulty(item.name)
        return 

        
    def getDifficulty(self, item):
        if (item == "chest"):
            header = QuestionText(self, "Select a Level", 45)
            header.anchor = "midtop"
            header.pos = (600,200)
            self.textList.append(header)
            
            prompt = QuestionText(self, "harder questions earn more points!", 30)
            prompt.anchor = "midtop"
            prompt.pos = (600,250)
            self.textList.append(prompt)
                                  
            self.difficulty_form = DifficultyForm(self)
            self.difficulty_form.easy.pos = (400, 350)
            self.difficulty_form.medium.pos = (550, 350)
            self.difficulty_form.hard.pos = (700, 350)
                                  
        elif (item == "gem"):
            self.current_question = self.GemList[random.randint(0,len(self.GemList)-1)]
            self.setNewQuestion()

    def easyClicked(self):
        self.current_question = self.ChestEasyList[random.randint(0,len(self.ChestEasyList)-1)]
        self.current_difficultyPoints = 10
        for i in self.textList:
            i.kill()
        self.difficulty_form.visible = False
        self.setNewQuestion()


    def mediumClicked(self):
        self.current_question = self.ChestMediumList[random.randint(0,len(self.ChestMediumList)-1)]
        self.current_difficultyPoints = 20
        for i in self.textList:
            i.kill()
        self.difficulty_form.visible = False
        self.setNewQuestion()

    def hardClicked(self):
        self.current_question = self.ChestHardList[random.randint(0,len(self.ChestHardList)-1)]
        self.current_difficultyPoints = 30
        for i in self.textList:
            i.kill()
        self.difficulty_form.visible = False
        self.setNewQuestion()

        
    def setNewQuestion(self):
        
        #question and answers
        question_text = QuestionText(self, self.current_question[0], 50)
        question_text.anchor = "midtop"
        question_text.pos = (600, 200)
        self.textList.append(question_text)
        
        a_text = QuestionText(self, self.current_question[1], 30)
        a_text.pos = (575, 305)
        a_text.anchor = "midleft"
        self.textList.append(a_text)

        b_text = QuestionText(self, self.current_question[2], 30)
        b_text.pos = (575, 405)
        b_text.anchor = "midleft"
        self.textList.append(b_text)

        c_text = QuestionText(self, self.current_question[3], 30)
        c_text.pos = (575, 505)
        c_text.anchor = "midleft"
        self.textList.append(c_text)
        
        #buttons
        self.question_form = QuestionForm(self)
        self.question_form.buttonA.pos = (500, 300)
        self.question_form.buttonB.pos = (500, 400)
        self.question_form.buttonC.pos = (500, 500)
        
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
        self.question_form.visible = False
        for i in self.textList:
            i.kill()
            
        self.finish_form = FinishForm(self)
        self.finish_form.finish.pos = (550,500)
            
        if (correct):
            answer_text = QuestionText(self, "Congratulations!", 50)
            sub_text = QuestionText(self, " you earned " + str(self.current_difficultyPoints) + " points!", 50)
        else:
            answer_text = QuestionText(self, "Incorrect", 50)
            sub_text = QuestionText(self, "Better luck next time!", 50)
            
        answer_text.pos = (600, 300)
        answer_text.anchor = "midtop"
        self.textList.append(answer_text)
        
        sub_text.pos = (600, 400)
        sub_text.anchor = "midtop"
        self.textList.append(sub_text)
        
        
    def setReturnScene(self, prev_scene):
        self.return_scene = prev_scene
        
    def returnScene(self):
        for i in self.textList:
            i.kill()
        spyral.director.replace(self.return_scene)
        print "return"
        return



        
class QuestionText(spyral.Sprite):
    def __init__(self, scene, text, size):
        super(QuestionText, self).__init__(scene)
        font = spyral.Font("libraries/spyral/resources/fonts/DejaVuSans.ttf", size)
        self.image = font.render(text, color=(0,0,0))
        
class QuestionForm(spyral.Form):
    buttonA = spyral.widgets.Button("Select ")
    buttonB = spyral.widgets.Button("Select ")
    buttonC = spyral.widgets.Button("Select ")
    
class FinishForm(spyral.Form):
    finish = spyral.widgets.Button("Finished ")
    
class DifficultyForm(spyral.Form):
    easy = spyral.widgets.Button(" EASY ")
    medium = spyral.widgets.Button(" MEDIUM ")
    hard = spyral.widgets.Button(" DIFFICULT ")


         
