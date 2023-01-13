import sys

while True :
    n = sys.stdin.readline().rstrip()
    if n == '0' :
        break
    if n == n[::-1] :
        print("yes")
    else :
        print("no")