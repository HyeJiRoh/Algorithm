import sys
input = sys.stdin.readline

width, height = map(int, input().split())

n = int(input())

w = [0, height]
h = [0, width]

for _ in range(n):
    check, value = map(int, input().split())
    if check == 0:
        w.append(value)
    elif check == 1:
        h.append(value)

w.sort()
h.sort()

w_max = 0
h_max = 0

for i in range(1, len(w)):
    if w[i] - w[i-1] > w_max:
        w_max = w[i] - w[i-1]

for j in range(1, len(h)):
    if h[j] - h[j-1] > h_max:
        h_max = h[j] - h[j-1]

result = w_max * h_max

print(result)