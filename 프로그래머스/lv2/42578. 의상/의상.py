def solution(clothes):
    closet = {}
    answer = 1
    
    for dress in clothes:
        if dress[1] in closet.keys():
            closet[dress[1]].append(dress[0])
        else:
            closet[dress[1]] = [dress[0]]
            
    for value in closet.values():
        answer *= len(value) + 1
    
    return answer-1