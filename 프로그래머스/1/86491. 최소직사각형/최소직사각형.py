def solution(sizes):
    answer = 0
    left_max, right_max = 0, 0
    
    for left, right in sizes:
        if left < right:
            left, right = right, left
            
        left_max = max(left_max, left)
        right_max = max(right_max, right)
    
    answer = left_max*right_max
    return answer