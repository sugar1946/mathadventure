myList = []
file = open('EasySubtraction.txt', 'r')
for line in file:
    q = line
    question = q.rstrip('\n')
    questionList = question.split(',')
    myList.append(questionList)

print myList

