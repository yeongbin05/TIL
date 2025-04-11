def backtrack(idx):
    if len(temp) == n:  # temp가 n 길이를 가졌다면 출력
        # print(temp)
        ans.append(temp[:])
        return
    for i in range(n):  # idx에서부터 n까지 반복
        if not visited[i]:  # 아직 방문하지 않았다면
            visited[i] = True
            temp.append(nums[i])  # 숫자 추가
            backtrack(i + 1)  # 다음 숫자 선택
            temp.pop()  # 백트래킹
            visited[i] = False  # 방문 표시 제거

n = int(input())  # n은 숫자의 개수
numbers = list(map(int, input().split()))  # 입력된 숫자 리스트

# nums가 1부터 n까지의 숫자로 되어 있다면
temp = []
ans = []
visited = [False] * n  # 방문 여부
nums = [i for i in range(1, n + 1)]  # nums를 1부터 n까지로 설정
backtrack(0)  # 백트래킹 시작
ans = sorted(ans)
if numbers[0] == 1:
    print(*ans[numbers[1]-1])
else:
    
    for i in range(len(ans)):
        if ans[i] == numbers[1:]:
            print(i+1)
