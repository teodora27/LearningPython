import math
n=int(input())
k=1+int(math.log2(n))
mb=(1<<k)-1
n=n^mb
nr=0
while n!=0:
    n=n&(n-1)
    nr+=1
print(nr)