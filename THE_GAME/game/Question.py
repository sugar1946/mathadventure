import spyral
import Item

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

    #def setQuestion(self):

#class QuestionText
