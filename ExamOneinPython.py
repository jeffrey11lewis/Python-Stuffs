import random
import math
print("hello")
print('picking sequence:')
ourNextNumber = 5
val = 1
useSequenceNumber = random.randrange(1,5,1)
print('use sequence number', useSequenceNumber)

print("Here is our sequence: , "( int(ourNextNumber))

if int(useSequenceNumber) == 1:
    startingPoint = random.randrange(1,10,1)
    termOne = int(startingPoint)
    termTwo = int(termOne + 2)
    termThree = int(termTwo + 2)
    termFour = int(termThree + 2)
    termFive = int(termFour + 2)
    ourNextNumber = termFive
    print('the sequence ', termOne, termTwo, termThree, termFour)
elif useSequenceNumber == 2:
    startingPoint = int(random.randrange(1,10,1))
    base = 2
    stepSize = int(random.randrange(1,4,1))
    term = startingPoint
    for x in range (0,5):

        nextTerm = term + stepSize
            print('term ', x+1, nextTerm)


else:
    print('that didnt work')



if (val == (ourNextNumber))
    print('you are correct')
else
    print('you are not correct')