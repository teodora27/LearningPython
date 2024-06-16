#1. Fie A un multiset format din n numere naturale nenule și S un număr natural nenul.
#Folosind metoda Backtracking, să se afișeze toate submultiseturile lui A care au suma
#elementelor egală cu S.
def back(subset,elem_ramase,S,rez):
    if(sum(subset)==S):
        rez.append(subset.copy())
        return
    for i in range(len(elem_ramase)):
        elem=elem_ramase[i]
        subset.append(elem)
        back(subset, elem_ramase[i+1:],S, rez)
        subset.pop()
def find_subseturi(A,S):
    result=[]
    back([],A,S,result)
    return result
def main():
    n=10
    S=8
    A=[1,2,3,4,5,6,7,8,9,10]
    print(find_subseturi(A,S))
main()