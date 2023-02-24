import math
import pdb

def factorize(number):
    factors = []
    div = list(range(1,number+1))
    for n in div:
        if number % n == 0:
            factors.append(n)
        else:
            continue
    return factors




m500 = 1 # As we can see the 7th triangle number has less than 7 factors, the 6th triangle number has less than 6 factors and so on. So I am going to assume that the 500th triangle number has less than 500 factors, so I can save calculus power.

t500 = int((m500*(m500+1))/2) # This is the 500th triangle number

#I create a while loop / I start with the th500 / then I calculate the number of factors until they are greater than 500
tn = t500
n = 1
#pdb.set_trace()
while len(factorize(tn)) <= 20 and n <= 16:
    n += 1
    tn = int(((n+1)*n)/2)
    print(f'{n}th, {tn}, {len(factorize(tn))}')






