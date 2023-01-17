import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    N = int(input())
    school = []
    alcohol = []

    for _ in range(N) :
        S, L = map(str, input().rstrip().split())
        school.append(S)
        alcohol.append(int(L))


    best = alcohol.index(max(alcohol))
    print(school[best])