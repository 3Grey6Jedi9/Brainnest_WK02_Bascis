import math
import numpy
import pdb

a = 1
b = 2
c = 1000 - a - b
final = []

#while (a**2 + 2**b) != (1000-a-b)**2:
    #a +=1
    #while b <= a:
        #b += 1



while (a**2 + 2**b) != (1000-a-b)**2:
    for n in list(range(1,1001)):
        a = n
        b = 2
        while b <= a:
            b +=1
        for m in list(range(b,1001)):
            b = m
            if (a**2 + 2**b) != (1000-a-b)**2:
                final = [a,b,c]
            else:
                continue

final[0]*final[1]*final[2]






def is_prime(number):
    if number < 2:
        return True
    for i in range(2,int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True





import math


def factorize(number):
    '''This fucntions returns a set with all the factors of a given number'''
    if is_prime(number):
        return {1,number}
    else:
        factors = set()
        div = set((range(1,number+1)))
        for n in div:
            if number % n == 0:
                factors.add(n)
            else:
                continue
        return factors


#Defining the initial variables

n = 1
tn = int((n*(n+1))/2)



def wloop(n,tn,fc):
    '''This function return the th number and its value that its number of factors is over a given number of factors.'''
    while len(factorize(tn)) <= fc:
        n += 1
        tn = int(((n+1)*n)/2)
    return n, tn

n, tn = wloop(n,tn,3)



print(f'{n}th, {tn}, {len(factorize(tn))}')











import math
a = 1
b = 2
c = 1000 - a - b
final = []

while (a**2 + 2**b) != (1000-a-b)**2:
    for n in list(range(1,1001)):
        a = n
        b = 2
        while b <= a:
            b +=1
        for m in list(range(b,1001)):
            b = m
            if (a**2 + 2**b) == (1000-a-b)**2:
                final = [a,b,c]
            else:
                continue

final[0]*final[1]*final[2]







