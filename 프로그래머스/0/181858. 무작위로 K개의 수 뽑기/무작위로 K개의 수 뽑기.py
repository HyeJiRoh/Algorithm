def solution(arr, k):
    result = []
    
    for num in arr :
        if num not in result :
            result.append(num)
    
    if len(result) < k:
        for _ in range(k - len(result)):
            result.append(-1)
    
    return result[:k]