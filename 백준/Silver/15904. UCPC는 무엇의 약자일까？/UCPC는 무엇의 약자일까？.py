import sys
input = sys.stdin.readline

str = list(input().strip())
ucpc = "UCPC"
index = 0

for word in str:
    if word in ucpc[index]:
        index += 1
    if index == 4:
        print("I love UCPC")
        break
else:
    print("I hate UCPC")