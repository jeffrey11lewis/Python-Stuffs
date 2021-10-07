import generateRandomNumber

generateRandomNumber.greetUser()
ourRandomNumber = generateRandomNumber.generateRandomNumber()
print('our random number is ', ourRandomNumber)





userWasRight = True





userGuess = generateRandomNumber.getUserGuess()

while (userWasRight):
   
    userWasRight = generateRandomNumber.wasAnswerCorrect(ourRandomNumber, userGuess)
    

    

while not userWasRight:
    generateRandomNumber.giveUserAHint(ourRandomNumber, userGuess)
    userWasRight = generateRandomNumber.wasAnswerCorrect(ourRandomNumber, userGuess)
    userGuess = generateRandomNumber.getUserGuess()
    
    