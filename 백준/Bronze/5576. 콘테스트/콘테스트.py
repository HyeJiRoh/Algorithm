import sys 
input = sys.stdin.readline 

w = []
k = []

for _ in range(10):
    w.append(int(input()))

for _ in range(10):
    k.append(int(input()))

w.sort(reverse=True)
k.sort(reverse=True)

w_sum = 0
k_sum = 0

for i in range(3):
    w_sum += w[i]
    k_sum += k[i]

print(w_sum, k_sum)