def solution(todo_list, finished):
    answer = []
    
    for idx in range(len(todo_list)):
        if finished[idx] == False:
            answer.append(todo_list[idx])        
    return answer