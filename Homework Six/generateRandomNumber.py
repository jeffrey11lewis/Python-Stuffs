import random
#from guessTheNumber import returnToThis
#import guessTheNumber

def greetUser():
    print("hello user")

def generateRandomNumber():
    random.seed(900)
    ourRandomNumber = random.randint(1,101)
    return ourRandomNumber




def getUserGuess():
    userGuess = input('please enter your guess between 1 and 100\n')
    #TODO: need to add some limits on what we let pass
    return userGuess

def wasAnswerCorrect(ourRandomNumber, userGuess):
    if(int(ourRandomNumber) == int(userGuess)):    
        
        print('you are correct')
        #return userWasRight
       

    else:
        print('you were not correct.')

def giveUserAHint(ourRandomNumber, userGuess):
    if(int(ourRandomNumber) > int(userGuess)):
        print('your number was too low.')
        print('try again:')
        #returnToThis()
    
    if (int(ourRandomNumber) < int(userGuess)):
        print('your number was too high.')
        print('try again:')
        getUserGuess()
