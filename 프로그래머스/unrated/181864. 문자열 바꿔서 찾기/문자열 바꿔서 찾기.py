def solution(myString, pat):
    result = ""
    for word in myString:
        if word == "A":
            result += "B"
        else:
            result += "A"
    return 1 if pat in result else 0