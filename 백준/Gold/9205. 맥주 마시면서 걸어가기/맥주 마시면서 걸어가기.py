import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    start_x, start_y = map(int, sys.stdin.readline().split()) 
    graph = []
    
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        graph.append([x, y]) 
    end_x, end_y = map(int, sys.stdin.readline().split()) 
    graph.append([end_x, end_y]) 
    visit = [False]*(n+1)
    
    def bfs():
        q = deque()
        q.append((start_x, start_y))
        while q:
            x, y = q.popleft()
            if abs(x - end_x) + abs(y - end_y) <= 1000: 
                print('happy')
                return
            for i in range(n):
                if not visit[i]:
                    nx, ny = graph[i] 
                    if abs(x-nx)+abs(y-ny)<=1000: 
                        q.append((nx, ny))
                        visit[i] = True
        print('sad') 
        return
    bfs()