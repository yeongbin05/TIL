import sys
input = sys.stdin.readline
k,n = map(int,input().split())
lan = [int(input()) for _ in range(k)]

start = 1 
end = max(lan)

while start <= end :
    mid = (start + end) //  2
    Sum = sum(l // mid for l in lan)
   
    if Sum >= n :
        start = mid + 1

    elif Sum < n :
        end = mid - 1

print(end)
        