import sys
input = sys.stdin.readline()

a, b = map(int, input.split())
result = (a+b)*(a-b)
print(result)