import re
def sol(text):
    lit=0
    LIT=0

    for chr in text:
        if(ord('a')<=ord(chr)&ord(chr)<=ord('z')):
            lit+=1
        if(ord('A')<=ord(chr)&ord(chr)<=ord('Z')):
            LIT += 1
    print("Litere mici: "+str(lit))
    print("Litere mari: "+str(LIT))
    semne = re.findall(r",|!|\.|'|\?", text)
    print(f"Semne de punctuatie: {len(semne)}")

def main():
    text=input()
    sol(text)

main()