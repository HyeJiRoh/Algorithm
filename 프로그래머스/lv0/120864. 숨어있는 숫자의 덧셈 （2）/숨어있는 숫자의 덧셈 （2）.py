import re

def solution(my_string):
    arr = re.findall(r'\d+', my_string)
    answer = 0
    
    for num in arr:
        num = int(num)
        answer += num
        
    return answer