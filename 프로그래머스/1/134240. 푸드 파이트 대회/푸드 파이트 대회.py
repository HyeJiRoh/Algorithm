def solution(food):
    answer = ''
    for idx in range(1, len(food)):
        for _ in range(food[idx]//2):
            answer += str(idx)
    
    return answer + '0' + answer[::-1]