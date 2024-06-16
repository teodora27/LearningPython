import re
def sol(text):
    cuv =[cuv.lower() for cuv in re.split(r"[^a-zA-Z]", text) if cuv !='']
    freq = {}
    for i in cuv:
        freq[i] = len(i)
    ls = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    file = open('grupe_cuvinte.txt', 'w')
    leng=ls[0][1]
    file.write(f"Lungime {leng}: {ls[0][0]}")
    for elem in ls[1:]:
        if elem[1]==leng:
            file.write(', '+elem[0])
        else:
            leng=elem[1]
            file.write(f"\nLungime {leng}: {elem[0]}")

def main():
    file = open('exemplu.txt','r')
    text= file.read()
    sol(text)

main()
