print("Enter a list of integers, separated with spaces:")
input = input()
input = input.split(' ')

total = 0
largestNumber = None

for num in input:
    num = int(num)
    total = total + num
    if largestNumber is None or num > largestNumber:
        largestNumber = num

print("The average of the", len(input), "inputted numbers is", total // len(input))
print("The largest number in the list is ", largestNumber)