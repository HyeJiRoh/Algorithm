def solution(answers):
    math_haters = [
        [1, 2, 3, 4, 5], 
        [2, 1, 2, 3, 2, 4, 2, 5], 
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    result = [0] * 3
    
    for idx, answer in enumerate(answers):
        for jdx, haters_answer in enumerate(math_haters):
            if answer == haters_answer[idx % len(haters_answer)]:
                result[jdx] += 1
                
    max_score = max(result)
    max_result = []
    
    for i, value in enumerate(result, start = 1):
        if value == max_score:
            max_result.append(i)
    
    return max_result

                