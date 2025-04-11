from collections import deque

def min_jumps_to_end(N, M, bad_stones):
    # bad_stones 배열을 set으로 바꾸어 체크 속도를 빠르게 함
    bad_set = set(bad_stones)
    
    # BFS 큐와 방문 체크 (visited[i][j]는 i번째 돌에 j칸 점프한 상태로 방문했는지 여부)
    visited = [[False] * (N + 1) for _ in range(N + 1)]
    queue = deque([(1, 1, 0)])  # (현재 돌 번호, 이전 점프 크기, 점프 횟수)
    visited[1][1] = True
    
    while queue:
        current, last_jump, jumps = queue.popleft()
        
        # 만약 현재 돌이 N번 돌이면, 점프 횟수 반환
        if current == N:
            return jumps
        
        # 갈 수 있는 다음 상태들 (current + last_jump - 1, current + last_jump, current + last_jump + 1)
        for delta in [-1, 0, 1]:
            next_jump = last_jump + delta
            if next_jump >= 1:  # 점프는 최소 1칸 이상이어야 함
                next_stone = current + next_jump
                if next_stone <= N and next_stone not in bad_set and not visited[next_stone][next_jump]:
                    visited[next_stone][next_jump] = True
                    queue.append((next_stone, next_jump, jumps + 1))
    
    return -1  # N번 돌에 도달할 수 없으면 -1을 반환

# 입력 처리
N, M = map(int, input().split())
bad_stones = [int(input()) for _ in range(M)]

# 결과 출력
print(min_jumps_to_end(N, M, bad_stones))
