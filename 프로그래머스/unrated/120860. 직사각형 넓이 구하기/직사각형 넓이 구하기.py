def solution(dots):
    max_x, min_x = max(dots)[0], min(dots)[0] 
    max_y, min_y = max(dots)[1], min(dots)[1]
    
    return (max_x - min_x) * (max_y - min_y)