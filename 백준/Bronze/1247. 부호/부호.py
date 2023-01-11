import sys
input = sys.stdin.readline

for i in range(3) :
    N = int(input())
    S = 0

    for k in range(N) :
        a = int(input())
        S += a

    if S == 0 :
        print("0")
    elif S > 0 :
        print("+")
    else :
        print("-")