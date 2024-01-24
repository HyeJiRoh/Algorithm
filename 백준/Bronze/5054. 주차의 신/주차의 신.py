import sys
input = sys.stdin.readline

t = int(input()) 

for _ in range(t) :
    n = int(input()) 
    shop = sorted(map(int, input().split()))

    print((shop[-1] - shop[0])*2)