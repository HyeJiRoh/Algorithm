def solution(participant, completion):
    hash_dict = {}
    sumHash = 0
    
    for i in participant:
        hash_dict[hash(i)] = i
        sumHash += hash(i)
        
    for j in completion:
        sumHash -= hash(j)

    return hash_dict[sumHash]