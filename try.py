import math
import random

def factorize(number):
    '''This function returns a set with all the factors of a given number'''
    x = 0
    c = 0
    y = 0
    if number < 2:
        return {1}
    factors = set()
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            factors.add(divisor)
            number //= divisor
        else:
            if divisor == 2:
                x = y = random.randint(1, 10)
                c = random.randint(1, 10)
            x = (x**2 + c) % number
            divisor = math.gcd(abs(x-y), number)
            if divisor > 1 and divisor != number:
                factors.add(divisor)
                number //= divisor
    factors.add(1)
    factors.add(number)
    return factors


# Defining the initial variables
n = 1
tn = int((n*(n+1))/2)

def wloop(n,tn,fc):
    '''This function returns the nth number and its value that has over a given number of factors'''
    while len(factorize(tn)) <= fc:
        n += 1
        tn = int(((n+1)*n)/2)
    return n, tn

n, tn = wloop(n,tn,5)

print(f'{n}th, {tn}, {len(factorize(tn))}')