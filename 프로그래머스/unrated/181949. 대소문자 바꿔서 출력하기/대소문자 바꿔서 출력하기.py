str = input()
result = ""

for i in str:
    if i.islower():
        i = i.upper()
        result += i
    else:
        i = i.lower()
        result += i

print(result)