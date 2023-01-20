import sys
input = sys.stdin.readline

while True :
    str = input().strip()
    base = str[0]
    sentence = str[1:]
    count = 0

    if base == '#' :
        break

    alpha = []
    alpha.append(base.lower())
    alpha.append(base.upper())

    for i in sentence :
        if i in alpha :
            count += 1

    print(base, count)