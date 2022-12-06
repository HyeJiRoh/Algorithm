def solution(before, after):
    answer = 0
    after = list(after)
    for i in before :
        if i in after :
            after.remove(i)
    if len(after) == 0 :
        answer = 1
    else :
        answer = 0
    return answer