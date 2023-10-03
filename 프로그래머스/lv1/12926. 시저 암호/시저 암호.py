def solution(s, n):
    answer = ''
    for word in s:
        if word.isupper() and ord(word) + n <= 90 or word.islower() and ord(word) + n <= 122:
            answer += chr(ord(word)+n)
        elif word.isupper() and ord(word) + n > 90 or word.islower() and ord(word) + n > 122:
            answer += chr(ord(word)+n-26)
        elif word == " ":
            answer += " "
    return answer