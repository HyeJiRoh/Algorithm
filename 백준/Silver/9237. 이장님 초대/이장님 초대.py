import sys
input = sys.stdin.readline

n = int(input())
tree = list(map(int, input().split()))
result = []

tree.sort(reverse=True)

for i in range(len(tree)):
    result.append(i+tree[i]+1)

print(max(result)+1)