def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    for check in reserve[:]:
        if check in lost:
            lost.remove(check)
            reserve.remove(check)
    
    for check in reserve:
        if check-1 in lost:
            lost.remove(check-1)
        elif check+1 in lost:
            lost.remove(check+1)
            
    return n - len(lost)