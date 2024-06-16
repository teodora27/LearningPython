def sol(str1, str2):
    freq = [0] * 30
    for char in str1:
        freq[int(ord(char) - ord('a'))] += 1

    for char in str2:
        freq[int(ord(char) - ord('a'))] -= 1
    for val in freq:
        if val != 0:
            return False

    return True


def main():
    str1 = input()
    str2 = input()
    print(sol(str1, str2))


main()
