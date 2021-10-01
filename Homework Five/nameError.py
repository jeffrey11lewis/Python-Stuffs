names = ['Bob', 'James', 'Ralph', 'Timothy', 'Cassandra', 'Sarah', 'Billy', 'Wolfeschlegelsteinhausenbergerdorff', 'Al']

print("Input an index number between the values of 0 and 8, including 0 and 8.")
index = int(input())

try:
    print('Name: {}'.format(names[index]))
except IndexError as nameException:
    print('Exception! {}'.format(nameException))

#using negative numbers up to -9 simply starts the list from the right side of the list.

    if index < 0:
        print('The closest name is: ' + names[0])

    else:
        print('The closest name is: ' + names[8])
