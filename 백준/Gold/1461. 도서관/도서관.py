import sys
input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))

negative_book = []
positive_book = []

for book in books:
    if int(book) < 0:
        negative_book.append(book)
    else:
        positive_book.append(book)
        
negative_book.sort()
positive_book.sort(reverse=True)

total = []

for i in range(0, len(negative_book), m):
    total.append(negative_book[i] * -1)
    
for i in range(0, len(positive_book), m):
    total.append(positive_book[i])

total.sort(reverse=True)
print(sum(total[1:])*2 + total[0])