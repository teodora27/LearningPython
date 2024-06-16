def main():
    n = 10
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    S = 8
    s = [-1] + [0] * (n * 5)

    mx = 0
    for i in range(1, n + 1):
        for j in range(mx, -1, -1):
            if 0 <= A[i - 1] + j < len(s) and s[A[i - 1] + j] == 0 and s[j] != 0:
                s[A[i - 1] + j] = A[i - 1]
                mx = max(A[i - 1] + j, mx)

    while(S):
        print (s[S],end=' ')
        S=S-s[S]
main()
