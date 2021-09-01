print('this program checks whether a string is a palindrome or not.')
print('\ninput your string to check:')
input = input()

inputString = input.replace(" ", "")
reverseString = inputString[::-1]

if inputString == reverseString:
    print('{} is a palindrome'.format(inputString))
else:
    print('{} is NOT a palindrome'.format(inputString))
