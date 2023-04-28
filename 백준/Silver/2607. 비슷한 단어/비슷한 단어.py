import sys
input = sys.stdin.readline

n = int(input())
base = list(input())
answer = 0

for _ in range(n-1):
    compare = base[:] 
    word = input() 
    count = 0

    for alphabet in word:
        if alphabet in compare:
            compare.remove(alphabet)
        else:
            count += 1

    if count < 2 and len(compare) < 2:
        answer += 1

print(answer)
