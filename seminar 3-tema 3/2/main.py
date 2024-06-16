def  sol(n,l):
    ans =[]
    for i in range(0,n):
        if l[i]>0:
            ans.append(l[i])
    print(ans)
def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    sol(n,l)
main()