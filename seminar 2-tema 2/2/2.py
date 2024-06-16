from collections import deque
def sol(str1, str2):
    str1, str2=str1.lower(), str2.lower()
    freq=[0]*30
    for chr in str1:
        freq[ord(chr)-ord('a')]+=1
    for chr in str2:
        freq[ord(chr)-ord('a')]-=1
    ok=0
    for val in freq:
        if val!=0:
            ok=1
            break
    if ok==1:
        print("Nu sunt anagrame")
    else:
        freq_str2 = []

        for i in range(30):
            freq_str2.append(deque())
        for i in range(0, len(str2)):
            freq_str2[ord(str2[i])-ord('a')].append(i)

        perm_str1=[]
        for char in str1:
            perm_str1.append(freq_str2[ord(char) - 97].popleft() + 1)
        return (perm_str1)


def main():
    str1=input()
    str2=input()
    print(sol(str1, str2))

main()