from collections import deque
N, M = map(int,input().split())

# N x N 방문 유무 확인 행렬 생성
visited = [[False] * M for _ in range(N)]
# N줄 만큼 입력
graph = [list(map(int, input().split())) for _ in range(N)]
# 상, 하, 좌, 우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

each = 0
result = []

def bfs(x, y):
  # 첫번째 들어온 좌표는 그림이므로 1로 잡아준다.
  count = 1
    # 범위 벗어나면 중단

  queue = deque()
  queue.append([x, y])  
  while queue:
    x, y = queue.popleft()
    # 상하좌우로 움직여본다
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
    # 범위 안에 있는데, 방문을 안했고, 값이 1이다면 그림으로 판단!
      if 0<=nx<N and 0<=ny<M:      
        if visited[nx][ny] == False and graph[nx][ny] == 1:
          count += 1
          visited[nx][ny] = True
          queue.append([nx, ny])
  return count
        


# 열
for x in range(N):
  # 행
  for y in range(M):
  # 현재 있는 위치가 그림이고, 방문을 안했으면? 시작!
    if graph[x][y] == 1 and visited[x][y] == False: 
      visited[x][y] = True
      pic = bfs(x,y)
      result.append(pic)


if len(result)==0:
    print(len(result))
    print(0)
else:
    print(len(result))
    print(max(result))