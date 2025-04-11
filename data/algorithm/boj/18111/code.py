import sys
input = sys.stdin.readline
n,m,b = map(int,input().split())
land = [list(map(int,input().split())) for _ in range(n)]

ans = float('inf')
ans_height = 0
min_height = min(map(min, land))
max_height = max(map(max, land))
for height in range(min_height, max_height + 1):
    temp_block_cnt = b
    temp_time = 0
    # temp_height = 0
    for i in range(n):
        for j in range(m):
            
            if land[i][j] > height :
                add = (land[i][j]-height)
                temp_block_cnt += add
                temp_time += add * 2
            else :
                pop = height - land[i][j]   
                temp_time += pop
                temp_block_cnt -= pop
    if temp_block_cnt < 0 :
        continue
    if temp_time < ans or (temp_time == ans and height > ans_height):
        ans = temp_time
        ans_height = height
print(ans,ans_height)


