def solution(s):
    answer = ''
    alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for idx, word in enumerate(alpha):
        if word in s:
            s = s.replace(word, str(idx))
        answer = s
    return int(answer)