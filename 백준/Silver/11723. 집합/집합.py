import sys
input = sys.stdin.readline

M = int(input())
S = set()

for i in range(M) :
    text = list(map(str, input().split()))

    if text[0] == "add" :
        if int(text[1]) not in S :
            S.add(int(text[1]))
    elif text[0] == "remove" :
        S.discard(int(text[1]))
    elif text[0] == "check" :
        if int(text[1]) in S :
            print(1)
        else :
            print(0)
    elif text[0] == "toggle" :
        if int(text[1]) in S :
            S.discard(int(text[1]))
        else :
            S.add(int(text[1]))
    elif text[0] == "all" :
        S.update([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    elif text[0] == "empty" :
        S = set()
