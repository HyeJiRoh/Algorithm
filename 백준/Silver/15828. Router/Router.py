from collections import deque

queue = deque([])
buffer_size = int(input())

while (True) :
  num = int(input())
  if num == -1 :
    break
  if num == 0 :
    queue.popleft()
  elif num !=0 and len(queue)<buffer_size :
    queue.append(num)

if len(queue) == 0 :
  print("empty")
else :
  for i in queue :
    print(i, end=" ")