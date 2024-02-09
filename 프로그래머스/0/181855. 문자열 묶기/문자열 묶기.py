def solution(strArr):
    arr = [0] * 100001
    for word in strArr:
        arr[len(word)] += 1
    
    return max(arr)