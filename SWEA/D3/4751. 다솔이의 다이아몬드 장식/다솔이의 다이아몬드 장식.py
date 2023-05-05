T = int(input())

for idx in range(1, T + 1):
    text = input()
    
    for i in range(len(text)):
        print("..#.", end = "")
    print(".")

    for i in range(len(text) * 2):
        print(".#", end = "")
    print(".")

    for i in text:
        print("#.%s."%i, end = "")
    print("#")

    for i in range(len(text) * 2):
        print(".#", end = "")
    print(".")

    for i in range(len(text)):
        print("..#.", end = "")
    print(".")