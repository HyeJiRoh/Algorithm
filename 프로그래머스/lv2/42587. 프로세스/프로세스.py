from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    answer = 0
    while queue:
        m = max(queue)
        l = queue.popleft()
        location -= 1 
        
        if l != m:
            queue.append(l)
            if location < 0:
                location = len(queue) -1
        else:
            answer += 1
            if location < 0:
                break
            
    return answer