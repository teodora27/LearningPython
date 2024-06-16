def creare_matrice(n):
    m=[]
    for i in range(n):
        lst=([0]*n)
        m.append(lst)
    for i in range(n):
        m[i][n-1]=1
        m[n-1][i]=1
    for i in range(n-2,-1,-1):
        for j in range(n-2,-1,-1):
            m[i][j]=m[i+1][j]+m[i][j+1]
    for i in range(n):
        print(m[i])
def main():
    n=4
    creare_matrice(n)
main()