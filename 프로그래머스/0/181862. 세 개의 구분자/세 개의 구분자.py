def solution(myStr):
    answer = []
    for word in ['a', 'b', 'c']:
        myStr = myStr.replace(word, ' ')
    answer = myStr.split()
    if not answer:
        answer = ['EMPTY']
    return answer