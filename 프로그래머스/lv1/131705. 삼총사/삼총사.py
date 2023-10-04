from itertools import combinations

def solution(number):
    answer = 0
    for num in combinations(number, 3):
        if sum(num) == 0:
            answer += 1
    return answer