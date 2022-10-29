student = [i for i in range(1, 31)]

for x in range(28):
  student.remove(int(input()))

print(min(student))
print(max(student))
