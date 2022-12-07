def solution(arr):
    answer = []
    if len(arr) > 1 :
        arr.remove(min(arr))
        answer = arr
    else :
        return [-1]
    return answer