t = int(input())  # 테스트 케이스 개수
for _ in range(t):
    n = int(input())  # 배열 크기
    nums = list(map(int, input().split()))  # 배열 X
    
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1,n):
        dp[i] = max(dp[i-1]+nums[i],nums[i])
        
    print(max(dp))