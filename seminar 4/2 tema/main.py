def pozitii():
    rez=[]
    colectie=(1, 2, -3, -4, 5, 6, 7)
    for i in range(0, len(colectie)):
        if int(colectie[i])>=0:
            rez.append(i+1)
    return rez
def semne():
    rez = []
    colectie = "sir, de /. caractere"
    for i in range(0, len(colectie)):
        if str(colectie[i]) in ",.;'/" :
            rez.append(i + 1)
    return rez

def ncif_ssum():
    rez = []
    colectie = (125, 79, 43, 74, 525, 46, 97)
    n=2
    s=16
    for i in range(0, len(colectie)):
        if len(str(colectie[i])) == n:
            nr=int(colectie[i])
            sum=0
            while nr:
                sum=sum+int(nr%10)
                nr=int(nr/10)
            if sum==s:
             rez.append(colectie[i])
    return rez

def cuv_lungime_n():
    lst=("ana","are","mere")
    lungime=3
    rez=[]

    for i in range(0, len(lst)):
        if(len(str(lst[i]))==lungime):
            rez.append(lst[i])
    return rez
def main():
    print(cuv_lungime_n())
main()