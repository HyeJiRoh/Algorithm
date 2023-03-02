while True:
    try:
        n = int(input())
        base = '1'

        while True:
            if int(base)%n == 0:
                print(len(base))
                break
            base += '1'

    except EOFError:
        break