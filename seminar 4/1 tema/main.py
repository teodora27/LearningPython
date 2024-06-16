def matrice(n):
    m=[]
    m=[[0]*(n-1)+[1]for i in range(0, n-1)]
    m.append([1]*(n))
    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            m[i][j]=m[i+1][j]+m[i][j+1]

    for linie in m:
        print (linie)
    print()
def main():
    n=5
    matrice(n)
main()