print('Enter Your First Name, Last Name, and Full Social ;)')

string_1 = input()
string_1 = string_1.split(' ')
first = string_1[0]
last = string_1[1]
number = int(string_1[2])

if len(last) > 5:
    last = last[:5]

print("Your Login Name: {}{}{}".format(last, first[0], number %100))