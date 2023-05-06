T = 10

for idx in range(1, T + 1):
    n = int(input())
    buildings = list(map(int, input().split()))

    view = []

    for i in range(2, n-2):
        value = min(buildings[i]-buildings[i-1], buildings[i]-buildings[i-2], buildings[i]-buildings[i+1], buildings[i]-buildings[i+2])
        
        if value >= 0:
            view.append(value)

    print("#%d %d"%(idx, sum(view)))
