import math

def is_prime(number):
    if number < 2:
        return True
    for i in range(2,int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

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

n = 2000
tn = int((n*(n+1))/2)



def wloop(n,tn,fc):
    '''This function return the th number and its value that its number of factors is over a given number of factors.'''
    while len(factorize(tn)) <= fc:
        n += 1
        tn = int(((n+1)*n)/2)
    return n, tn

n, tn = wloop(n,tn,300)



print(f'{n}th, {tn}, {len(factorize(tn))}')