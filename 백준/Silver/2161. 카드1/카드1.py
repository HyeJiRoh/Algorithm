import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
cards = deque(list(i for i in range(1, n + 1)))
result = []

while len(cards) != 1:
    result.append(cards.popleft())
    cards.append(cards.popleft())

for i in result:
    print(i, end = " ")
print(cards[0])