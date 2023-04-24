import math

def solution(arr):
    answer = arr[0]
    
    for num in arr:
        answer = answer*num // math.gcd(answer, num)
        
    return answer