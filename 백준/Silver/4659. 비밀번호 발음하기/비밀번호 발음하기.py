vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    s = input()
    if s == "end":
        break
    v_cnt = 0
    v_repeat, c_repeat = 0, 0
    last = ''
    flag = True

    for i in s:
        if i in vowel:
            if v_repeat == 2 or ((i != 'e' and i != 'o') and last == i):
                flag = False
                break
            else:
                v_repeat += 1
                c_repeat = 0
                v_cnt += 1
                last = i

        else:
            if c_repeat == 2 or last == i:
                flag = False
                break
            else:
                c_repeat += 1
                v_repeat = 0
                last = i
    if v_cnt == 0:
        flag = False

    if flag:
        print("<{}> is acceptable.".format(s))
    else:
        print("<{}> is not acceptable.".format(s))