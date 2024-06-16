import re
def sol(nr):
    numere=[i for i in re.split(r"[^0-9]", nr)]
    freq=[0]*10
    for nr in numere:
        for chr in nr:
          freq[ord(chr)-ord('0')]+=1
    maxim=''
    for i in range(9, 0, -1):
        for j in range(0, freq[i]):
            maxim+=str(i)
    print(maxim)
    minim=''
    for i in range(1, 9):
        if freq[i]>=1:
            minim+=str(i)
            freq[i]-=1
            break
    for i in range(0,9):
        for j in range(0, freq[i]):
            minim+=str(i)
    print(minim)

def main():
    file=open('numere.txt','r')
    nr=file.read()
    sol(nr)
main()