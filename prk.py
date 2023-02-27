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





















