def solution(n):
    answer = 0
    left = 0
    right = 0
    numbers = [i for i in range(1, n+1)]
    
    while left <= right <= n:
        if sum(numbers[left:right]) == n:
            answer += 1
            right += 1
        elif sum(numbers[left:right]) > n:
            left += 1
        else:
            right += 1
            
    return answer