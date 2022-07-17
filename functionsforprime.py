import math

def isPerfectlyDivisible(numerator, denominator):
    return numerator % denominator == 0

def isOdd(value):
    return value % 2 == 1

def isEven(value):
    return(value %2 == 0)

def isPerfectSquare(value):
    sqr = math.sqrt(value)
    return(math.floor(sqr) == sqr)

def isPerfectCube(value):
    cub = value**(1/3)
    return(math.floor(cub) == cub)

def isPrime(value):
    for i in range(2, value-1):
        if isPerfectlyDivisible(value, i):
            return False
    return True

for i in range(1, 10000):
    if (isPrime(i)):
        print(i)
    #print(i)
    #print(isOdd(i))
    #print(isEven(i))
    #print(isPerfectSquare(i))
    #print(isPerfectCube(i))
