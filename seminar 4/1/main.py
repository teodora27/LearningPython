def matrice_triunghiulara(n, m):
    for i in range(1, n):
        m.append([i]+[0]*(i-1))
    m.append([i for i in range (n, 0, -1)])
    for i in range (n-2,0, -1):
        for j in range(1,i+1):
            m[i][j]=m[i+1][j]+m[i][j-1]+m[i+1][j-1]
    print(m)

def afisare(m):
    nrmax=max([len(str(max(linie))) for linie in m])
    for linie in m:
        for elem in linie:
            print(str(elem).rjust(nrmax), end=' ')
        print()
def main():
    #n=int(input())
    n=4
    m = []
    matrice_triunghiulara(n, m)
    afisare(m)

main()