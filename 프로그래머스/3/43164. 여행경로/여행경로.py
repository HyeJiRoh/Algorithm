from collections import defaultdict

def solution(tickets):
    travel = defaultdict(list)
    
    for key, value in tickets:
        travel[key].append(value)
        
    for city in travel:
        travel[city].sort()
        
    answer = dfs(travel)
    
    return answer

def dfs(travel):
    answer = []
    arr = ["ICN"]
    
    while arr:
        tmp = arr[-1]
        
        if tmp not in travel or len(travel[tmp]) == 0:
            answer.append(arr.pop())
        else:
            arr.append(travel[tmp].pop(0))
            
    return answer[::-1]