def suma(nr):
    nr=int(nr)
    s=0
    while nr>0:
        s=s+int(nr%10)
        nr=int(nr/10)
    return s
def citire_matrice(fisier):
    fin=open(fisier, "r")
    n=int(fin.readline())
    rad=1
    while rad*rad<n:
        rad+=1
    lst=[]
    nr=0
    lista=[]
    for linie in fin:
        nr=linie.split()
        nr=int(nr[0])
        lista.append(nr)
        if len(lista)==rad:
            lst.append(lista)
            lista=[]
    return lst
def prelucrare_matrice(lst):
    n=len(lst)
    lst2=[]
    for i in range(0,n):
        diag=lst[i][i]
        lista=[]
        for j in range(0, n):
            nr=int(lst[i][j])
            nr=nr-diag
            if i!=j:
                lista.append(nr)
        lst2.append(lista)
    return(lst2)
def main():
    nume="matrice.in"
    lst=citire_matrice(nume)
    print(lst)
    lst2=prelucrare_matrice(lst)
    print(lst2)
    n=len(lst2)
    for i in range(0, n):
        for j in range(0, n-1):
            print(lst2[i][j], end=' ')
        print()
    k=7
    fisierout=open("numere.out","w")
    n=len(lst)
    rez=[]
    for i in range(0, n):
        for j in range(0, n):
            if( suma(int(lst[i][j])))==k:
                rez.append(lst[i][j])
    rez.sort()
    for elem in rez:
        print(elem,file=fisierout, end=' ')

main()