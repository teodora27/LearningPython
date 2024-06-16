def citire_liste(fisier):
    fin = open(fisier, "r")
    n=int(fin.readline().strip())
    lista=[]
    for i in range(n):
        lista.append([])
    for linie in fin:
        rand=linie.split()
        x=int(rand[0])
        y=int(rand[1])
        lista[y].append(x)

    return(lista)
def prelucrare_liste(L, x):
    for i in range(len(L)):
        if x in L[i]:
            while x in L[i]:
                L[i].remove(x)
    rez=[]
    for lista in L:
        if len(lista)>1:
            rez.append(lista)
    return rez
def nr_div(x):
    nr=0
    for d in range(1, x+1):
        if x%d==0:
            nr+=1
    return nr
def main():
    fisier="liste.in"
    L=(citire_liste(fisier))
    x=0
    rez=(prelucrare_liste(L,x))
    for lista in rez:
        for elem in lista:
            print(elem, end=' ')
        print()
    ans=[]
    k=int(input())
    for lista in rez:
        for elem in lista:
            if nr_div(elem)==k:
                if elem not in ans:
                 ans.append(elem)
    ans.sort(reverse=True)
    for elem in ans:
        print (elem)
main()