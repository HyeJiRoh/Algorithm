import sys
input = sys.stdin.readline

while True :
    sentence = input().strip()
    moeum = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0

    if sentence == '#' :
        break

    for i in sentence :
        if i in moeum :
            count += 1

    print(count)