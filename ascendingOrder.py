my_list = []
my_string_array = input().split()
n = len(my_string_array)
for i in range(0, n):
    element = int(my_string_array[i])
    if element > 0:
        my_list.append(element)
my_list.sort()
print(my_list)