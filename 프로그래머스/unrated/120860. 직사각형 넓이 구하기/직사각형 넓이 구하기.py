def solution(dots):
    max_x, min_x = max(dots[i][0] for i in range(len(dots))), min(dots[i][0] for i in range(len(dots)))
    max_y, min_y = max(dots[i][1] for i in range(len(dots))), min(dots[i][1] for i in range(len(dots)))
    
    return (max_x - min_x) * (max_y - min_y)