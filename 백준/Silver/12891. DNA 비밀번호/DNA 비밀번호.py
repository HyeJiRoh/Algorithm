from collections import deque

s, p = map(int, input().split())
DNA = list(str(input()))
A, C, G, T = map(int, input().split())

dna_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

left, right = 0, p-1

arr = deque(DNA[left:right])

for i in arr:
    dna_dict[i] += 1

cnt = 0

while right < s:
    dna_dict[DNA[right]] += 1

    if dna_dict['A'] >= A  and dna_dict['C'] >= C and dna_dict['G'] >= G and dna_dict['T'] >= T:
        cnt += 1

    dna_dict[DNA[left]] -= 1 
    left += 1
    right += 1

print(cnt)