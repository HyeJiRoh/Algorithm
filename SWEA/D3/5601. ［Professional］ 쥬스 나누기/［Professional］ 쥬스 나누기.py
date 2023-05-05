T = int(input())

for idx in range(1, T + 1):
    n = int(input())
    print("#%d"%idx, end = " ")
    
    for _ in range(n):
        print("%d/%d"%(1, n), end = " ")
    
    print("")