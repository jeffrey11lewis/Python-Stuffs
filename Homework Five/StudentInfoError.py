class StudentInfoError(Exception):
    def __init__(self, message):
        self.message = message

def findID(ID, info):
  #  print("looking up " + ID)
    if ID in info:
      #  print("THere is a match in dictionary.")
        
        #print(info[ID])

        return info[ID]
    raise StudentInfoError('NO STUDENT ID FOR ' + str(name.upper()))

# WE ARE BROKEN HERE
def findName(name, info):
    #print("are you getting here?")
    for name in info:
        if name == info[name]:
            return name

    raise StudentInfoError('NO STUDENT NAME FOR ' + str(ID))
  
if __name__ == '__main__':
    studentInfo = {
        'Reagan' : 'rebradshaw835',
        'Ryley' : 'rbarber894',
        'Peyton' : 'pstott885',
        'Tyrese' : 'tmayo945',
        'Caius' : 'ccharlton329'
    }

print("please enter [ID] or [name]")
print("When typing [ID], you are looking for NAME (so enter ID)")
print("When typing [name], you are looking for ID (so enter name)")
userChoice = input()



    
try:
    if userChoice.lower() == 'name':
        print("Please enter a name to lookup:")
        name = input()
        result = findID(name, studentInfo)
        print("The ID found is " + result)

    elif userChoice.upper() == 'ID':
        #print("we are looking for Name")
        print("Please enter an ID to lookup:")
        ID = input()
        result = findName(ID, studentInfo)
        print("The Name FOUND is " + result)


    else:
        print("NO")
except StudentInfoError as InfoError:
    print(InfoError)