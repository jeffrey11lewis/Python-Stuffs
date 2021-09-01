print("Temperature Converter - Rudimentary Edition")
print('enter the temperature you are converting from:') 
print('F(1) C(2)\nK(3) R(4)')
fromTemp = input()



print('enter the temperature you are converting to:')
print('F(1) C(2)\nK(3) R(4)')
toTemp = input()


#print('Enter Your Value to Calculate FROM:') 
#input = input()

print(type(fromTemp))
print(type(toTemp))


if int(fromTemp) == 1 & int(toTemp) == 2:
    print("it is working")
else:
    print('shit dont work.')


#
#°C = (°F - 32) × 5/9
##cValue = ((int(input)) - 32) * (5/9)
#°R = °F + 459.67
#rValue = (int(input)) + 459.67
#(°F − 32) × 5/9 + 273.15 = K
#kValue = ((int(input)) -32) * (5/9) + 273.15


#print((str(cValue)) + " Degrees Celsius")
#print(((str(rValue))) + " Degrees Rankine")
#print ((str(kValue)) + " Degrees Kelvin")