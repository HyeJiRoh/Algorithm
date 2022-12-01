def solution(my_string):
    answer = ''
    moeum = ['a', 'e', 'i', 'o', 'u']
    
    for i in my_string :
        if i not in moeum :
            answer += i
    return answer