import sys
input = sys.stdin.readline

n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

if numbers[1] - numbers[0] == numbers[2] - numbers[1]:
    value = numbers[1] - numbers[0]
    print(numbers[n - 1] + value)
else:
    value = numbers[1] // numbers[0]
    print(numbers[n - 1] * value)
