str = input()
reverse_str = str[::-1]

length = len(str)
for i in range(length):
    if str[i:] == reverse_str[0 : length - i]:
        print(length + i)
        break
