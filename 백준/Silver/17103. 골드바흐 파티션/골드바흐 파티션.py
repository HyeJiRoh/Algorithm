import sys
input = sys.stdin.readline

T = int(input())
prime = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        for j in range(2 * i, 1000001, i):
            check[j] = 1

for _ in range(T):
    N = int(input())
    cnt = 0 
    
    for i in prime:
        if i >= N:
            break
        if not check[N - i] and i <= N - i: 
            cnt += 1
    
    print(cnt)
