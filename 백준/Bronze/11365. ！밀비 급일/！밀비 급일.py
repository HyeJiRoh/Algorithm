import sys
input = sys.stdin.readline

while True :
    str = input().strip()

    if str == "END" :
        break

    print(str[::-1])