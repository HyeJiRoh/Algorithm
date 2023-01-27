import sys
input = sys.stdin.readline

money = int(input())
count = 0

while True :
    if money%5 != 0 :
        money -= 2
        count += 1
    else :
        money -= 5
        count += 1

    if money <= 0 :
        break

if money == 0:
    print(count)
else :
    print(-1)