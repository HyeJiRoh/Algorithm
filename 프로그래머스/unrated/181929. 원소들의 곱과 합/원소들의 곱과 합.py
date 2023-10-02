def solution(num_list):
    answer = 0
    multi = 1
    add = 0
    
    for num in num_list:
        multi *= num
        add += num
    
    if multi < add**2 :
        answer = 1
        
    return answer