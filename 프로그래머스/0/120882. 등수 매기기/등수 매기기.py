def solution(score):
    answer = []
    tmp = []
    result = []
    
    for score_value in score:
        total = sum(score_value)
        answer.append(total)
        tmp.append(total)
    answer.sort(reverse=True)
    
    for t in tmp:
        if t in answer:
            result.append(answer.index(t)+1)
    return result