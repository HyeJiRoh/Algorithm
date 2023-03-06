import sys
input = sys.stdin.readline

n = int(input())
books = {}

for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] +=1

max_book = max(books.values())

best_seller=[]

for book, number in books.items():
    if number == max_book:
        best_seller.append(book)

print(sorted(best_seller)[0])
