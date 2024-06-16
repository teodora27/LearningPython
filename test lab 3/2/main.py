def adauga_bucati(dict, nume_spiridus, nume_jucarie, nr_buc):
    if nume_spiridus:
        if nume_jucarie in dict[nume_spiridus]:
            dict[nume_spiridus][nume_jucarie]+=int(nr_buc)
        else:
            dict[nume_spiridus][nume_jucarie] = int(nr_buc)
    else:
        for i in range(len(dict[nume_spiridus])):
            dict[nume_spiridus][i]+=int(nr_buc)
    nr=0
    for jucarie in dict[nume_spiridus]:
        print(jucarie)
        nr=nr+int(dict[nume_spiridus][jucarie])
    for elem in dict:
        print(elem, dict[elem])
    print(nr)

def ordonare(t):
    return -len(t[1]),-int(t[2]), t[0]
def top_spiridusi(dict, nume, nr_min):
    rez=[]
    for spiridusi in nume:
        nr=0
        lst_jucarii=[]
        for jucarii in dict[spiridusi]:
            if int(dict[spiridusi][jucarii])>=nr_min:
                lst_jucarii.append(jucarii)
                lst=[]
                if spiridusi not in lst:
                    lst.append(spiridusi)
                nr=nr+int(dict[spiridusi][jucarii])
        if len(lst_jucarii)>=1:
            lst.append(lst_jucarii)
            lst.append(nr)
        if len(lst)>=1:
            if lst not in rez:
             rez.append(lst)
    rez.sort(key=ordonare)
    return (rez)



def main():
    fin=open("spiridusi.in","r")
    dict={}
    for linie in fin:
        rand=linie.split(" : ")
        elem=rand[1].split()
        numar=elem[len(elem)-1]
        elem.remove(numar)
        cuv=''
        for x in elem:
            cuv+=x
            cuv+=' '
        cuv=cuv[:-1]
        nume=rand[0]
        if nume not in dict:
            dict[nume]={}
            if cuv not in dict[nume]:
                dict[nume][cuv]=int(numar)
            elif cuv in dict[nume]:
                dict[nume][cuv]+=int(numar)

        else:
            if cuv not in dict[nume]:
                dict[nume][cuv]=int(numar)
            elif cuv in dict[nume]:
                dict[nume][cuv]+=int(numar)


    lista_nume=["Spiridus Harnic","Spiridus Poznas","Spiridus Jucaus"]
    for elem in dict:
        print(elem, dict[elem])
    print()
    nume_spiridus = "Spiridus Poznas"
    nume_jucarie = "papusa"
    adauga_bucati(dict, nume_spiridus, nume_jucarie, 1)


main()