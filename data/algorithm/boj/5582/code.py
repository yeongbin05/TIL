s = input()
t = input()
n, m = len(s), len(t)

arr = [[0] * (m + 1) for _ in range(2)]
ans = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s[i - 1] == t[j - 1]:
            arr[1][j] = arr[0][j - 1] + 1
            ans = max(ans, arr[1][j])
        else:
            arr[1][j] = 0
    arr[0], arr[1] = arr[1], [0] * (m + 1)  # 현재 행을 이전 행으로, 새로운 행 초기화

print(ans)
