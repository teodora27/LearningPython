def interval_dreapta(t):
    return int(t[0]), -int(t[1])

def main():
    fin = open("autostrada.in")
    prima_linie = fin.readline()
    lungime = int(prima_linie.split()[0])
    intervale = []

    for linie in fin:
        aux = linie.split()
        intervale.append((int(aux[0]), int(aux[1])))

    fin.close()
    intervale.sort(key=interval_dreapta)
    print("Intervale:", intervale)

    rez = [intervale[0]]
    nr = 0

    for pereche in intervale:
        if rez[nr][1] >= pereche[0]:
            if pereche[1]>rez[nr][1]:
             rez[nr] = (rez[nr][0], pereche[1])
        else:
            rez.append(pereche)
            nr += 1

    rez_tuple = tuple(rez)
    suma=0
    for pereche in rez:
        suma+=int(pereche[1])-int(pereche[0])
    print(suma/lungime*100)
    print("Rezultat:", rez_tuple)

main()
