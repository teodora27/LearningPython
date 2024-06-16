def nr_vocale(cuv):
    nr=0
    for litera in cuv:
        if litera=='a' or litera=='e' or litera=='i' or litera=='o' or litera=='u':
            nr+=1
    return nr
def citire_siruri(nume_fisier):
    fin=open(nume_fisier,"r")
    lst=[]
    for linie in fin:
        rand=linie.strip()
        lst.append(rand)
    return lst

def prelucrare_siruri(lst, n):
    i=0
    for lista in lst:
        elemente=lista.split(' ')
        cuvant=' '
        for cuv in elemente:
            litera=cuv[len(cuv)-1]
            cuvant+=litera
        lst[i]+=(cuvant)
        i+=1
    lst2=[]
    for lista in lst:
        noua_lista=[]
        elemente = lista.split(' ')
        for cuv in elemente:
            if(nr_vocale(cuv)>=n):
                noua_lista.append(cuv)
        lst2.append(noua_lista)

    print(lst2)
def punctuld(lst, w):
    rez=[]
    for lista in lst:
        elemente=lista.split(' ')
        for cuv in elemente:
            if w in cuv:
                if cuv not in rez:
                 rez.append(cuv)
    rez1=sorted(rez)
    return rez1
def main():
    fisier="date.in"
    lst=(citire_siruri(fisier))
    n=3
    prelucrare_siruri(lst, n)
    w=str(input())
    print(w)
    print(lst)
    print(punctuld(lst, w))

main()