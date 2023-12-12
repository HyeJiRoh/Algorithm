def solution(participant, completion):
    dict = {}
    total = 0
    
    for name in participant:
        dict[hash(name)] = name
        total += hash(name)
    
    print(dict)
    
    for j in completion:
        total -= hash(j)

    return dict[total]