n=int(input())
lst = list(map(int, input().strip().split()))[:n]
#print(lst)
if len(lst)>1:
    print(0)
else:
    print(lst[0])