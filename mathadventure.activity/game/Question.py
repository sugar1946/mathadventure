# -*- coding: utf-8 -*-

#import spyral
import random

class Question():
    def __init__(self):
        self.theList = theList
        self.makeList('Question Files/HardWordProblems.txt', aList)

    def makeList(self,filename, alist):
        file = open(filename, 'r')
        for line in file:
            q = line
            question = q.rstrip('\n')
            qList = question.split(';')
            alist.append(qList)

    def addNumbers(self,alist):
        names = ['Rai’zhana','Rikesh','Richard','Khalil','David','Moises','Angela','Lamar','Aiyana','Raymond','Rafiqe','Khadejah','Aaliyah','Fahim','Shanyia','Anashiah','Makyiah','Neonyae','Ceyrah']
        food = ['apple','orange','cake', 'pie','pastry']
        n = random.choice(names)
        f1 = random.choice(food)
        f2 = random.choice(food)
        f3 = random.choice(food)
        f4 = random.choice(food)
        n1 = random.randint(2,10)
        nless = random.randint(1,n1)
        nmore = random.randint(n1,99)
        nmore2 = random.randint(nmore,100)

        for i in range(0, len(alist[0])):
            stringtochange = alist[0][i]
            print stringtochange
            replacements = {'name':str(n),'food1':str(f1),'food2':str(f2),'food3':str(f3), 'food4':str(f4),'num1':str(n1),'numless':str(nless),'nummore':str(nmore),'nummore2':str(nmore2)}
            newstring = str(stringtochange).format(**replacements)
            alist[0][i] = newstring
            print newstring





