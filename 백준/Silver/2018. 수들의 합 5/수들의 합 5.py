import sys
input = sys.stdin.readline

n = int(input())

start = 0
end = 0

result = 0
count = 0

while end <= n:
    if result < n:
        end += 1
        result += end
    elif result > n:
        result -= start
        start += 1
    else:
        count += 1
        end += 1
        result += end

print(count)