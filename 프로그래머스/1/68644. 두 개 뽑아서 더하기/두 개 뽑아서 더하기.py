def solution(numbers):
    tmp_arr = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            tmp_arr.append(numbers[i] + numbers[j])
    
    result = sorted(list(set(tmp_arr)))
    
    return result