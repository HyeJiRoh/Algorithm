import sys
input = sys.stdin.readline;

board = input().strip()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if board.count('X') >=1 :
    print(-1)
else:
    print(board)