import generateRandomNumber

generateRandomNumber.greetUser()
ourRandomNumber = generateRandomNumber.generateRandomNumber()
print('our random number is ', ourRandomNumber)





userWasRight = True





userGuess = generateRandomNumber.getUserGuess()
def returnToThis():

    while (userWasRight):
    
        print('your guess was: ', str(userGuess))
        userWasRight = generateRandomNumber.wasAnswerCorrect(ourRandomNumber, userGuess)

        

    if not userWasRight:
        generateRandomNumber.giveUserAHint(ourRandomNumber, userGuess)
        userWasRight = False