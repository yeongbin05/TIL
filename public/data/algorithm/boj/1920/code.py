"""
https://www.acmicpc.net/problem/1920

문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

# 첫 예상 : 이진 탐색

# 틀린 부분
1. end = n-1을 n으로 설정해서 틀림
2. while start<=end 를 start < end로 함
"""

n = int(input())
n_arr = list(map(int,input().split()))
n_arr.sort()
m = int(input())
m_arr = list(map(int,input().split()))

for i in m_arr :
    start = 0
    end = n - 1
    while (start<=end):
        middle = (start+end) // 2
        # print(start,end,middle)
        if i > n_arr[middle] :
            start = middle + 1
            
        elif i < n_arr[middle] :
            end = middle - 1
            

        else :
            print(1)
            break
    
    else :
        print(0)