def recur(board):
    length = len(board)
    first = board[0][0]
    for i in range(length):
        for j in range(length):
            if board[i][j] != first:
                half = length // 2

                # 4개의 구역 생성
                top_left = [row[:half] for row in board[:half]]
                top_right = [row[half:] for row in board[:half]]
                bottom_left = [row[:half] for row in board[half:]]
                bottom_right = [row[half:] for row in board[half:]]

                return f"({recur(top_left)}{recur(top_right)}{recur(bottom_left)}{recur(bottom_right)})"
                
    return int(first)
n = int(input())
pixel = [input() for _ in range(n)]
temp = pixel[0][0]

ans = recur(pixel)
print(ans)
