import random
#from guessTheNumber import returnToThis
#import guessTheNumber

def greetUser():
    print("hello user")

def generateRandomNumber():
    random.randint(1,101)
    ourRandomNumber = random.randint(1,101)
    return ourRandomNumber




def getUserGuess():
    userGuess = input('please enter your guess between 1 and 100\n')
    #TODO: need to add some limits on what we let pass
    return userGuess

def wasAnswerCorrect(ourRandomNumber, userGuess):
    if(int(ourRandomNumber) == int(userGuess)):    
        
        print('you are correct')
        exit()

        
       

    else:
        print('')

def giveUserAHint(ourRandomNumber, userGuess):
    if(int(ourRandomNumber) > int(userGuess)):
        print('your number was too low.')
       # print('try again:')
        #anotherGuess = input()
       # return anotherGuess
    
    if (int(ourRandomNumber) < int(userGuess)):
        print('your number was too high.')
        #print('try again:')
        #getUserGuess()
