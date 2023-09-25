answer = int(input())

while True:
    operator = input()
    if operator == "=":
        break
    num = int(input())
    if operator == "+":
        answer += num
    elif operator == "-":
        answer -= num
    elif operator == "*":
        answer *= num
    elif operator == "/":
        answer //= num
print(answer)
