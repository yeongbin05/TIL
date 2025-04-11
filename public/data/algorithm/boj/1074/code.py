def recur(map):
    global cnt
    n = len(map)
    print(map)
    if n <= 2:
        return
    left_up = [i[:n//2] for i in map[:n//2]]
    left_down = [i[:n//2] for i in map[n//2:]]
    right_up = [i[n//2:] for i in map[:n//2]]
    right_down = [i[:n//2] for i in map[n//2:]]

    return recur(left_up),recur(right_up),recur(left_down),recur(right_down)
n,r,c = map(int,input().split())
board = [[_] * (2**n) for _ in range(2**n)]
cnt = 0
recur(board)