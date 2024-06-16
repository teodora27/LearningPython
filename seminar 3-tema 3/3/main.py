def sol(ls_carti):
    for i in range(len(ls_carti)):
        if int(ls_carti[i][2])<2000:
            ls_carti[i]+=(False,)
        else:
            ls_carti[i]+=(True,)
    for i in range(len(ls_carti)):
        if 0 not in ls_carti[i]:
            print(ls_carti[i])
    #print(ls_carti)
def main():
    ls_carti=[("Carte1",("Autor1", "Autor2"), 2001, 50),
          ("Carte2",("Autor1"), 1999, 50),
          ("Carte3",("Autor1", "Autor2"), 2000, 50)]
    sol(ls_carti)
main()