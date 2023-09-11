import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

stack = [[], [], [], []]

flag = True

for num in A:
    for i in range(4):
        if not stack[i]:
            stack[i].append(num)
            break
        else:
            if stack[i][-1] < num:
                stack[i].append(num)
                break
    else:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
