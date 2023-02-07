import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

left = 0
right = n-1

total = abs(arr[left] + arr[right])
result = [arr[left], arr[right]]

while left < right:
    left_tmp = arr[left]
    right_tmp = arr[right]

    sum = left_tmp + right_tmp

    if abs(sum) < total:
        total = abs(sum)
        result = [left_tmp, right_tmp]

        if total == 0:
            break

    if sum < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])