n = int(input())

cups = [1, 2, 3]
for _ in range(n):
    x, y = map(int, input().split())
    
    x_index = cups.index(x)
    y_index = cups.index(y)
    
    cups[x_index], cups[y_index] = cups[y_index], cups[x_index]
    
print(cups[0])