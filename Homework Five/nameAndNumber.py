parts = input().split()

name = parts[0]

while name != 'stop':
    try:
        age = int(parts[1]) + 1
    except:
        age = 0
    print(name, age)

    parts = input().split()
    name = parts[0]
    