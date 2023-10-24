def solution(spell, dic):
    for word in dic:
        if set(spell) == set(word):
            return 1
    return 2