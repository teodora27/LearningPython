def sortrare(t):
    return -t[3], t[0], t[1]
def premiati(dict, scoruri, k):
    rez=[]
    for echipe in dict:
        for strumfi in dict[echipe]:
            print(strumfi)
            numar = 0
            rasp=[]
            suma=0
            for nr in dict[echipe][strumfi]:
                 nr=int(nr)
                 if nr in scoruri:
                    numar+=1
                    rasp.append(nr)
                    rasp.sort()
                    suma+=nr

            if numar>=k:
                print(numar)
                lst=[]
                lst.append(echipe)
                lst.append(strumfi)
                lst.append(rasp)
                suma/=numar
                suma = round(suma, 2)
                lst.append(suma)
                if lst not in rez:
                    rez.append(lst)
    rez.sort(key=sortrare)
    print(rez)
def stergere(dict, echipa, membru):
    dict2={}
    for echipe in dict:
        if echipe!=echipa:
            dict2[echipe]=dict[echipe]
        else:
            if len(dict[echipe])<=2:
                print("am sters si celalat jucator")
            else:
                dict2[echipe]={}
                for membri in dict[echipe]:
                    if membri !=membru:
                        dict2[echipe][membri]=dict[echipe][membri]
    print(dict2)
def main():
    fin=open("punctaje.in","r")
    dict={}
    for linie in fin:
        rand=linie.split()
        if rand[0]=="Echipa":
            cuv=""
            for i in range(1,len(rand)):
                cuv+=rand[i]
                cuv+=" "
            cuv=cuv[:-1]
            if cuv not in dict:
                dict[cuv]={}
        else:
            i=0
            nume=""
            while rand[i]!=':':
                nume =nume+rand[i]+" "
                i+=1
            if nume not in dict[cuv]:
                dict[cuv][nume]=[]
            for j in range(i+1,len(rand)):
                dict[cuv][nume].append(rand[j])


    print(dict)
    scoruri=[50, 25, 40, 60, 30, 45]
    #premiati(dict, scoruri,3)
    stergere(dict,"Potiuni magice","Papa Strumf ")

main()