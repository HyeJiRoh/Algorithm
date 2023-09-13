import sys
input = sys.stdin.readline

N, G = input().split()
player = [input() for _ in range(int(N))]
player = list(set(player))

if G == 'Y' :
    print(len(player))
elif G == 'F' :
    print(len(player) // 2)
elif G == 'O' :	
    print(len(player) // 3)