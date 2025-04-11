"""
https://www.acmicpc.net/problem/9019

처음 예상 : bfs
"""
from collections import deque
def D(n):
    n *= 2
    if n > 9999 :
        return n % 10000
    
    return n

def S(n):
    if n == 0 :
        return 9999
    
    return (n - 1)
    
def L(n):
    n = str(n)[1:] + str(n).pop(0)
    
    return int(n)
def R(n):
    n = str(n)[1:] + str(n).pop()
    
    return n
t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
