import sys
input = sys.stdin.readline;

n = int(input())
guest = []

for num in range(n):
    num = int(input())
    guest.append(num)

guest.sort(reverse=True)

tip = 0

for idx in range(n):
    guest[idx] -= idx
    if guest[idx] > 0:
        tip += guest[idx]

print(tip)