#IT Ticket Generator

string_1 = input()
userInput = string_1.split(' ')


print('NOUN, VERB(present) , NOUN, VERB')

if(userInput[1] != 'quit'):

    print("I'm sorry to bother you with this again, but my", userInput[0], "is still having problems with ", userInput[1], "\nHonestly, this has to be on your end. The only thing I've spilled on it was", userInput[2],"about three months ago, but I don't think that would cause it to", userInput[3])
  #  print('eating', userInput[0], userInput[1], 'a day keeps the doctor away.')