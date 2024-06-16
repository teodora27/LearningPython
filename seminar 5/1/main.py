def cheieExtremitateDreapta(interval):
     return interval[1]

fin = open("intervale.txt")
intervale = []
for linie in fin:
    aux = linie.split()
    intervale.append((int(aux[0]), int(aux[1])))
fin.close()
intervale.sort(key=cheieExtremitateDreapta)
M = [intervale[0][1]]
for icrt in intervale[1:]:
    if icrt[0] > M[len(M)-1]:
        M.append(icrt[1])
fout = open("acoperire.txt", "w")
fout.write("\n".join([str(x) for x in M]))
fout.close()