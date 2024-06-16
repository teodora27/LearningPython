#Optimizați algoritmul de la
# problema anterioară,utilizând metoda
# programării dinamice pentru a determina
# lungimea maximă a unui subșir crescător
# al șirului dat .

def lungime_cel_mai_lung_subsir_crescator(a):
    n=len(a)
    lungimi=[1]*n
    for i in range(1, n):
        for j in range(i):
            if a[i]>a[j] and lungimi[i]<lungimi[j]+1:
                lungimi[i]=lungimi[j]+1
    return max(lungimi)

def valid(subsir, lungime_max):
    if len(subsir)<lungime_max:
        return False
    for i in range(1,len(subsir)):
        if subsir[i]<subsir[i-1]:
            return False
    return True
def back(subsir, elem_ramase,rez,lungime_max):
    for i in range(len(elem_ramase)):
        elem=elem_ramase[i]
        subsir.append(elem)
        if valid(subsir, lungime_max):
            rez.append(subsir.copy())
        back(subsir,elem_ramase[i+1:],rez,lungime_max)
        subsir.pop()

def main():
    a=[1,0,2,7,5,6,8,3,10]
    rez=[]
    lungime_max = lungime_cel_mai_lung_subsir_crescator(a)
    print(lungime_max)
    back([],a,rez,lungime_max)
    print(rez)

main()
