T = int(input())

for idx in range(1, T + 1):
    a, b = map(int, input().split())

    if a < b :
        print("#%d"%idx, "<")
    elif a == b :
        print("#%d"%idx, "=")
    else:
        print("#%d"%idx, ">")