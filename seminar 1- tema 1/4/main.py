#variante 1
n=int(input())
if (n!=0) & (n&(n-1)==0):
        print(n)
else:
    nr=0
    while n!=0:
         n=n>>1
         nr+=1
    print(2**nr)

#varianta 2
'''
import math
n=int(input())
a=int(math.log2(n))
if 2**a==n:
    print(2**a)
else:
    print(2**(a+1))
'''