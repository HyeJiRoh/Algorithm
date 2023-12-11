def solution(participant, completion):
    dict = {}
    total = 0
    
    for i in participant:
        dict[hash(i)] = i
        total += hash(i)
        
    for j in completion:
        total -= hash(j)

    return dict[total]