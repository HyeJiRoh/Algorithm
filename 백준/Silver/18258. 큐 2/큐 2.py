import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
queue = deque([])

for i in range(n) :
  txt = input().split()
  if txt[0] == 'push' :
    queue.append(txt[1])
  elif txt[0] == 'pop' :
    if len(queue) == 0 :
      print(-1)
    else : 
      print(queue.popleft())
  elif txt[0] == 'size' :
    print(len(queue))
  elif txt[0] == 'empty' :
    if len(queue) == 0 :
      print(1)
    else :
      print(0)
  elif txt[0] == 'front' :
    if len(queue) == 0 :
      print(-1)
    else :
      print(queue[0])
  elif txt[0] == 'back' :
    if len(queue) == 0 :
      print(-1)
    else :
      print(queue[-1])