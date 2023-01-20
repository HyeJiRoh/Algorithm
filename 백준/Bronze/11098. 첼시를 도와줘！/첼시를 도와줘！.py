import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n) :
    p = int(input())
    player_list = []

    for _ in range(p) :
        price, name = map(str, input().strip().split())
        price = int(price)
        player_list.append([price, name])
        player_list.sort(reverse=True, key = lambda x:x[0])

    print(player_list[0][1])