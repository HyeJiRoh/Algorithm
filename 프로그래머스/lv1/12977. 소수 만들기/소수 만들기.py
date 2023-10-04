from itertools import combinations

def solution(nums):
    answer = 0
    for num in combinations(nums, 3):
        data = sum(num)
        flag = True
        
        for i in range(2, data):
            if data % i == 0:
                flag = False
                break
                
        if flag:
            answer += 1
            
    return answer