import math
def sayHello():
    print('hello')

def isNumberPrime(numberToCheck):
    placeToStopLooking= math.floor(numberToCheck/2)
    

    for divisorCheck in range(2, placeToStopLooking):
        if numberToCheck % divisorCheck == 0:
            print('turns out that ', numberToCheck, 'was not prime...')
            return False
    print("we found a prime! ", numberToCheck, 'is prime.')
    return True

def countPrimesLessThan(numberRange):
    print('we want to know how many numbers less than ', numberRange, ' are prime.')

    numberOfPrimes = 0
    for numberToCheck in range(2, numberRange):
            print('we are looking at ', numberToCheck)
            if isNumberPrime(numberToCheck):
                print("confirmed we have a prime")
                numberOfPrimes += 1

    print('we found ', numberOfPrimes, 'primes less than ', numberRange)