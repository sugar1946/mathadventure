import spyral

class Question_text(spyral.sprite):
    def __init__(self, scene, questionText):
        font = spyral.Font("libraries/spyral/resources/fonts/DejaVuSans.ttf", 40)
        self.image = font.render(questionText,color=BLACK)

class Question(spyral.scene):
    def __init__(self, scene):
        super(Question, self).__init__(self)

    #def setText(self):

    def setLists(self):
        easySubtraction = []
        file = open('EasySubtraction.txt', 'r')
        for line in file:
            q = line
            question = q.rstrip('\n')
            questionList = question.split(',')
            easySubtraction.append(questionList)



       
