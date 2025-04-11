# https://www.acmicpc.net/problem/1759
import sys
input = sys.stdin.readline
def count_vowels(s):
    vowels = "aeiou"  # 대소문자 모음
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
def count_consonant(s):
    consonant = "bcdfghjklmnpqrstvwxzy"  # 대소문자 모음
    count = 0
    for char in s:
        if char in consonant:
            count += 1
        
    return count
def back(idx,temp):
    if len(temp) == L :
        vowel_count = count_vowels(temp)
        consonant_count = len(temp) - vowel_count
        if vowel_count >= 1 and consonant_count >= 2:
            ans.append(''.join(temp))
        return
    
    for i in range(idx,C):
        temp.append(chars[i])
        back(i + 1, temp)
        temp.pop()
L,C = map(int,input().split())
chars = input().split()
chars.sort()
temp,ans = [],[]
back(0,temp)
for i in ans:
    print(''.join(i))