def solution(myString, pat):
    answer = ''
    idx = myString.rfind(pat)
    return myString[:idx+len(pat)]