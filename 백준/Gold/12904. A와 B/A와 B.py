import sys

input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

flag = False

while T:
    if T[-1] == "A":
        T.pop()
    elif T[-1] == "B":
        T.pop()
        T = T[::-1]
    if S == T:
        flag = True
        break

if flag:
    print(1)
else:
    print(0)
