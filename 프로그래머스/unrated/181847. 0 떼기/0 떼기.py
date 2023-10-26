def solution(n_str):
    start = 0
    for i in range(len(n_str)):
        if n_str[i] != '0':
            start = i
            break
            
    return n_str[start:]