import sys

N = int(sys.stdin.readline().rstrip())
base = list(sys.stdin.readline().rstrip())

for i in range(N-1) :
    str = list(sys.stdin.readline().rstrip())
    for k in range(len(base)) :
        if base[k] != str[k] :
            base[k] = '?'

print(''.join(base))