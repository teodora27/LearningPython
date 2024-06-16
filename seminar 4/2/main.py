def este_anagrama(sir, anagrama):
    dict={}
    dict2={}
    for litera in anagrama:
        if litera not in dict:
            dict[litera]=0
        if litera in dict:
            dict[litera]+=1
    for litera in sir:
        if litera not in dict2:
            dict2[litera] = 0
        if litera in dict:
            dict2[litera] += 1
    for litera in dict:
        if litera not in dict2:
            return False
        if litera in dict2 and dict2[litera]!=dict[litera]:
            return False
    return True

def functie_generica(lst, anagrama):
    rez=[]
    for cuv in lst:
        if(este_anagrama(anagrama, cuv)):
            rez.append(cuv)
    print(rez)

def main():
    fin=open("date.in","r")
    linie=fin.readline().split()
    n=int(linie[0])
    anagrama=str(linie[1])
    lst=[]
    for linie in fin:
        lst.append(linie.strip())
    functie_generica(lst,anagrama)
main()