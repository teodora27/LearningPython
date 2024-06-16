def sol(n):
    M = [[0]*(n-1)+[1] for i in range(1, n)]
    M.append([1 for i in range(0,n)])
    for i in range(n-2,-1, -1):
        for j in range(n-2, -1, -1):
            M[i][j]=M[i+1][j]+M[i][j+1]
    for i in range(0,n):
        print (M[i])
def main():
    n = int(input())
    sol(n)
main()