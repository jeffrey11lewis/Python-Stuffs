import math

def quadraticFormula(a,b,c):
    x1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
    return(x1, x2)

def printNumber(number, prefixString):
    if float(int(number)) == number:
        print("{}{:.0f}".format(prefixString, number))
    else:
        print("{}{:.2f}".format(prefixString, number))

if __name__ == '__main__':
    print("This program calculates an answer based upon the quadratic formula.\n")
    print('Please enter your a:')
    a = float(input())
    print('Please enter your b:')
    b = float(input())
    print('Please enter your c:')
    c = float(input())

    solution = quadraticFormula(a,b,c)

print("Solutions to {:.0f}x^2 + {:.0f} = 0".format(a,b,c))
printNumber(solution[0], "x1 = ")
printNumber(solution[1], "x2 = ")