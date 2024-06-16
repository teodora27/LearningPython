def crescator(subsir):
    ok=1
    for i in range(1,len(subsir)):
        if subsir[i]<subsir[i-1]:
            ok=0
    return ok
def back(subsir, elem_ramase,rez):
    for i in range(len(elem_ramase)):
        elem=elem_ramase[i]
        subsir.append(elem)
        if crescator(subsir):
            rez.append(subsir.copy())
        back(subsir,elem_ramase[i+1:],rez)
        subsir.pop()

def main():
    a=[1,0,2,7,5,6,8,3,10]
    rez=[]
    back([],a,rez)
    lungime_max=0
    for subsir in rez:
        if len(subsir)>lungime_max:
            lungime_max=len(subsir)

    raspuns=[]
    for subsir in rez:
        if len(subsir)==lungime_max:
            raspuns.append(subsir)
    print(raspuns)

main()
