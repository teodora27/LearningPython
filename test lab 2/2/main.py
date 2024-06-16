def sortare(t):
    return t[0], -float(t[2]), t[1]
def sortare123(t):
    return -float(t)
def rezultate(dict, probe, N):
    rez=[]
    raspuns = ()
    for participant in dict:
        for proba in dict[participant]:
            if proba in probe:
                if len(dict[participant][proba]) >= N:
                    raspuns = []
                    raspuns.append(proba)
                    raspuns.append(participant)
                    medie = 0
                    count = 0
                    nr_ramase = []

                    lst=dict[participant][proba]
                    lst.sort(key=sortare123)
                    del lst[0]
                    del lst[len(lst)-1]

                    for nr in lst:
                        nr_ramase.append(nr)
                        medie += float(nr)
                        count += 1


                    medie = medie / count
                    medie=round(medie,2)
                    raspuns.append(medie)
                    nr_ramase.sort()
                    raspuns.append(nr_ramase)
            if raspuns not in rez:
                rez.append(raspuns)
    return rez
def adaugare(dict, num_proba, nume_concurent, lista_nr):
    if nume_concurent in dict:
        if num_proba in nume_concurent:
            dict[nume_concurent][num_proba].append(lista_nr)
            return len(dict[nume_concurent])
    return "Numele probei sau al concurentului nu exista!"

def main():
    fin=open("concurs.in","r")
    dict={}
    for linie in fin:
        ln=(linie.strip(' ').split())
        if len(ln)==1:
            nume=str(ln[0])
            if nume not in dict:
                dict[nume]={}
        else:
            proba=ln[0]
            if proba not in dict[nume]:
                dict[nume][proba]=[]
            for i in range(1, len(ln)):
                dict[nume][proba].append(ln[i])
   # print(dict)
 #   probe=('trambulina','greutati')
 #   N=5
  #  rez=rezultate(dict,probe,N)
#    rez.sort(key=sortare)
 #   for lst in rez:
  #      print(lst)
    linie =input()
    nm=linie.split()
    p=nm[0]
    c=nm[1]
    a=[]
    for i in range(2,len(nm)):
        a.append(nm[i])
    print(adaugare(dict,p,c,a))

main()