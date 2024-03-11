def solution(keyinput, board):
    
    x, y = 0, 0
    
    for i in range(0, len(keyinput)):
        if keyinput[i] == "up":
            y += 1
            if y > board[1] / 2:
                y -= 1
        elif keyinput[i] == "down":
            y -= 1
            if -(board[1] / 2) > y:
                y += 1
        elif keyinput[i] == "left":
            x -= 1
            if -(board[0] / 2) > x:
                x += 1
        elif keyinput[i] == "right":
            x += 1
            if x > board[0] / 2:
                x -= 1
                
    return [x, y]