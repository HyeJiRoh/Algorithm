import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cards = list(map(int, input().split()))
cards.sort()

for _ in range(m):
    value = cards[0] + cards[1]
    cards[0] = value
    cards[1] = value
    cards.sort()

result = 0

for value in cards:
    result += value

print(result)