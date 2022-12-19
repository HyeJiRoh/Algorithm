def solution(array, n):
    answer = 0
    differ = 100
    array.sort()
    
    for i in array :
        if abs(n-i) < differ :
            differ = abs(n-i)
            answer = i

    return answer
