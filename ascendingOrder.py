print('Enter a list of numbers, both negative and nonnegative, separated with spaces: ')
input = input()

stringOfNumbers = input.split()

inputtedNumbers = []

for token in stringOfNumbers:
    if int(token) >= 0:
        inputtedNumbers.append(int(token))

inputtedNumbers.sort()

for values in inputtedNumbers:
    print(values, end = ' ')