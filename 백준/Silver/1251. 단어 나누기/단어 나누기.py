s = input()

result = []

for i in range(len(s)-2):
    for j in range(i + 1, len(s) - 1):
        for k in range(j + 1, len(s)):
            check = s[:j][::-1] + s[j:k][::-1] + s[k:][::-1]
            result.append(check)

print(min(result))
