def solution(answers):
    answer_lists = [
        [1, 2, 3, 4, 5], 
        [2, 1, 2, 3, 2, 4, 2, 5], 
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    results = [0] * 3
    
    for i, answer in enumerate(answers):
        for j, answer_list in enumerate(answer_lists):
            if answer == answer_list[i % len(answer_list)]:
                results[j] += 1
    
    max_result = max(results)
    final_result = []
    
    for i, result in enumerate(results):
        if result == max_result:
            final_result.append(i + 1)
    
    return final_result