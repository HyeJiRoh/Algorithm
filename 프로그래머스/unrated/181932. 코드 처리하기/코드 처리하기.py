def solution(code):
    answer = ''
    mode = 0
    
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] != "1" and idx % 2 == 0:
                answer += code[idx]
            elif code[idx] == "1" and mode == 0:
                mode = 1        
        elif mode == 1: 
            if code[idx] != "1" and idx % 2 != 0:
                answer += code[idx]
            elif code[idx] == "1" and mode == 1:
                mode = 0
    
    if len(answer) == 0:
        return "EMPTY"
    
    return answer