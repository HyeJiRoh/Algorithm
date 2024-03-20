def solution(N, stages):
    player = [0] * (N+2)
    
    for stage in stages:
        player[stage] += 1
    
    fail_rate = {}
    total = len(stages)
    
    for i in range(1, N+1):
        if player[i] == 0:
            fail_rate[i] = 0
        else:
            fail_rate[i] = stages.count(i) / total
            total -= player[i]
            
    result = sorted(fail_rate, key = lambda x: fail_rate[x], reverse = True)
    
    return result