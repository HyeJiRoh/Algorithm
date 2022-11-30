def solution(sides):
    answer = 0
    sides.sort()
    sum = int(sides[0])+int(sides[1])
    if sum <= sides[2] :
        answer = 2
    elif sum > sides[2] :
        answer = 1
    return answer