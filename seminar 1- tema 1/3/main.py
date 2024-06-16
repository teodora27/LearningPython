x, y = map(int, input().split())
x=x^y
nr=0
while(x):
    nr+=1
    x=x&(x-1)
print(nr)