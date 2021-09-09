print("Enter a list of integers, separated with spaces:")
input = input()
input = input.split(' ')

total = 0
largestNumber = None

#https://www.w3schools.com/python/ref_keyword_none.asp
""""
The None keyword is used to define a null value, or no value at all.

None is not the same as 0, False, or an empty string. None is a data type of its own (NoneType) and only None can be None.
"""

for num in input:
    num = int(num)
    total = total + num
    if largestNumber is None or num > largestNumber:
        largestNumber = num

print("The average of the", len(input), "inputted numbers is", total // len(input))
print("The largest number in the list is", largestNumber)