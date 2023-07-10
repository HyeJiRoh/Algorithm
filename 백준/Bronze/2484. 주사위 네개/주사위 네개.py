N = int(input())
A = [ sorted(list(map(int,input().split()))) for _ in range(N) ]
prize = 0 

def check(arr):
    return len(set(arr))

for a in A:
    money = 0
    if check(a) == 1:
        money += 50000 + a[0]*5000
    elif check(a) == 2:
        if a[1] == a[2]:
            money += 10000 + a[1]*1000
        else:
            money += 2000 + 500*(a[1]+a[2])
    elif check(a) == 3:
        for i in range(1,len(a)):
            if a[i] == a[i-1]:
                money += 1000 + a[i]*100
    else:
        money += a[-1]*100
    prize = max(prize, money)

print(prize)