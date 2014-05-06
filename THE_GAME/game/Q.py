# -*- coding: utf-8 -*-
import spyral
import random
from fractions import Fraction

class Question(spyral.Sprite):
    def __init__(self, scene, character):
        super(Question, self).__init__(scene)
        ##self.thisScene = scene
        self.image = spyral.Image(filename=('game/images/question.bmp'))
        self.pos = (350,50)
        self.layer = 'top'
        #self.getDifficulty()
        self.player = character
        self.sceneReturn = scene

        #question lists
        self.chestEasyList = []
        self.makeList('game/Question Files/EasyWordProblems.txt',self.chestEasyList)
        self.chestMediumList = []
        self.makeList('game/Question Files/MediumWordProblems.txt',self.chestMediumList)
        self.chestHardList = []
        self.makeList('game/Question Files/HardWordProblems.txt',self.chestHardList)

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
                            
    def makeList(self,filename, alist):
        file = open(filename, 'r')
        for line in file:
            q = line
            question = q.rstrip('\n')
            qList = question.split(';')
            alist.append(qList)
        self.addNumbers(alist)

    def addNumbers(self,alist):
        names = ['Rai’zhana','Rikesh','Richard','Khalil','David','Moises','Angela','Lamar','Aiyana','Raymond','Rafiqe','Khadejah','Aaliyah','Fahim','Shanyia','Anashiah','Makyiah','Neonyae','Ceyrah']
        food = ['apple','orange','cake', 'pie','pastry','cookie', 'apricot','mango', 'sushi', 'salmon', 'sandwhich', 'pizza', 'bacon', 'steak']
        numslow = range(3,12)
        numshigh = range(13,50)
        
        n = random.choice(names)
        names.remove(n)
        nam2 = random.choice(names)
        
        f1 = random.choice(food)
        food.remove(f1)
        f2 = random.choice(food)
        food.remove(f2)
        f3 = random.choice(food)
        food.remove(f3)
        f4 = random.choice(food)
        
        n1 = random.choice(numslow)
        numslow.remove(n1)
        n2 = random.choice(numslow)
        numslow.remove(n2)
        n3 = random.choice(numslow)
        t = n1+n2+n3
        
        nless1 = random.randint(2,n1-1)
        nless2= random.randint(2,n1-1)
        nless3= random.randint(2,n3-1)

        orderFrac1 = Fraction(random.randint(1,2), random.randint(9,12))
        orderFrac2 = Fraction(random.randint(2,3), random.randint(4,8))
        orderFrac3 = random.choice([Fraction(7,8),Fraction(8,9), Fraction(7,9),Fraction(4,5), Fraction(5,6)])
        
        fracforSub = Fraction(int(nless1/2), n1)
        fracEasy = Fraction(nless2,n1)
        frac1 = Fraction(nless1,n1)
        frac2 = Fraction(nless2,n2)
        frac3 = Fraction(nless3,n3)
        frac7 = Fraction(nless1-2,n1)
        fracAdd = frac1 + fracEasy
        fracSub = frac1 - fracforSub
        fracMult = frac1*fracEasy
        fracDiv = frac1/fracEasy
        
        fracAdd2 = frac1 + frac2
        fracSub2 = frac1 - frac2
        fracMult2 = frac1*frac2
        fracDiv2 = frac1/frac2
        
        nmore1 = random.randint(n1+1,15)
        nmore2 = random.randint(n2+1,15)
        nmore3 = random.randint(n3+1,15)
        nmorem = random.randint(nmore1+1,100)

        for j in range(0,len(alist)):
            for i in range(0,len(alist[j])):
                stringtochange = alist[j][i]
                replacements = {'name':str(n),'name2':str(nam2),'food1':str(f1),'food2':str(f2),'food3':str(f3), 'food4':str(f4),
                                'num1':str(n1),'num2':str(n2),'num3':str(n3), "total":str(t),'numless1':str(nless1),'numless2':str(nless2),'numless3':str(nless3),
                                'nummore1':str(nmore1),'nummore2':str(nmore2),'nummore3':str(nmore3),'nummoreM':str(nmorem),
                                'fraction1':str(frac1), 'fractionEasy':str(fracEasy),'fractionforSub':str(fracforSub), 'fraction2':str(frac2),'fraction3':str(frac3),
                                'orderedFraction1':str(orderFrac1),'orderedFraction2':str(orderFrac2),'orderedFraction3':str(orderFrac3),
                                'otherFraction':str(frac7),
                                'fractionAdd':str(fracAdd),'fractionSub':str(fracSub),'fractionMult':str(fracMult), 'fractionDiv':str(fracDiv),
                                'fractionAdd2':str(fracAdd2),'fractionSub2':str(fracSub2),'fractionMult2':str(fracMult2)}

                newstring = str(stringtochange).format(**replacements)
                alist[j][i] = newstring

    def easyClicked(self):
        self.current_question = self.chestEasyList[random.randint(0,len(self.chestEasyList)-1)]
        self.current_difficultyPoints = 10
        self.setNewQuestion()


    def mediumClicked(self):
        self.current_question = self.chestMediumList[random.randint(0,len(self.chestMediumList)-1)]
        self.current_difficultyPoints = 20
        self.setNewQuestion()

    def hardClicked(self):
        self.current_question = self.chestHardList[random.randint(0,len(self.chestHardList)-1)]
        self.current_difficultyPoints = 30
        self.setNewQuestion()

        
    def setNewQuestion(self):
        self.image = spyral.Image(filename=('game/images/blank_question.bmp'))
        #question and answers
        questionlines = self.current_question[0].split('.')
        z = 175
        for i in range(0,len(questionlines)):
            question_text = QuestionText(questionlines[i], 18).getImage()
            self.image.draw_image(question_text, position = (10,z))
            z += 25

        self.answerList = self.current_question[1:4]
            
        self.current_question[1] = random.choice(self.answerList)
        self.answerList.remove(self.current_question[1])
        a = "A) " + self.current_question[1]
        a_text = QuestionText(a, 20).getImage()
        self.image.draw_image(a_text, position = (75,z+25))

        b1 = random.choice(self.answerList)
        self.answerList.remove(b1)
        self.current_question[2] = b1
        b = "B) "+ str(b1)
        b_text = QuestionText(b, 20).getImage()
        self.image.draw_image(b_text, position = (75,z+75))

        c1 = random.choice(self.answerList)
        self.current_question[3] = c1
        c = "C) "+ str(c1)
        c_text = QuestionText(c, 20).getImage()
        self.image.draw_image(c_text, position = (75,z+125))
        
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
        self.image = spyral.Image(filename=('game/images/feedback.bmp'))
        if (correct):
            answer_text = QuestionText("Congratulations!", 30).getImage()
            sub_text = QuestionText( " you earned " + str(self.current_difficultyPoints) + " points!", 25).getImage()
            self.player.updateScore(self.current_difficultyPoints)
        else:
            answer_text = QuestionText("I'm Sorry", 30).getImage()
            sub_text = QuestionText("The correct answer is " + str(self.current_question[4]) , 25).getImage()
            tipLines = self.current_question[5].split('.')
            s = 200
            for i in range(0, len(tipLines)):
                tip_text = QuestionText(tipLines[i], 15).getImage()
                self.image.draw_image(tip_text, position = (50, s))
                s += 30
                                      
        self.image.draw_image(answer_text, position = (100,100))
        self.image.draw_image(sub_text, position = (100,150))

    def returnScene(self):

        self.sceneReturn.setCharacter(self.player,self.player.ani_array)

        self.kill()
        self.scene.defreezeMonster()

        
class QuestionText(spyral.Image):
    def __init__(self, text, size):
        font = spyral.Font("libraries/spyral/resources/fonts/DejaVuSans.ttf", size)
        self.image = font.render(text, color=(0,0,0))
    def getImage(self):
        return self.image


        



         
