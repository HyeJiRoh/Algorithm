from collections import deque

def solution(arr):
    answer = []
    queue = deque(arr)
    answer.append(queue.popleft())
    
    while len(queue):
        if answer[-1] != queue[0]:
            answer.append(queue.popleft())
        else:
            queue.popleft()
        
    return answer