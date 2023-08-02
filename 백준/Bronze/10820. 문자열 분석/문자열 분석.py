while True:
    try:
        lower_case, upper_case, number, blank = 0, 0, 0, 0
 
        for i in input():
            if i.islower():
                lower_case += 1
            elif i.isupper():
                upper_case += 1
            elif i.isdigit():
                number += 1
            else:
                blank += 1
        print(lower_case, upper_case, number, blank)
 
    except EOFError:
        break