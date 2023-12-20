def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if arr[i] == 2:
            answer.append(i)
    
    if len(answer) != 0:
        return arr[min(answer):max(answer)+1]
    else:
        return [-1]