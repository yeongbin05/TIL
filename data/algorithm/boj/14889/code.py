# https://www.acmicpc.net/problem/14889

import sys
from itertools import combinations

def calc_team_score(team, S):
    score = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            score += S[team[i]][team[j]] + S[team[j]][team[i]]
    return score

def backtrack(N, S):
    people = list(range(N))
    min_diff = sys.maxsize

    # 모든 사람 중 N/2명을 고르는 조합을 생성
    for start_team in combinations(people, N//2):
        # 링크 팀은 start_team에 포함되지 않은 사람들
        start_team = set(start_team)
        link_team = set(people) - start_team
        
        # 각 팀의 능력치 계산
        start_team_score = calc_team_score(list(start_team), S)
        link_team_score = calc_team_score(list(link_team), S)
        
        # 능력치 차이 계산
        diff = abs(start_team_score - link_team_score)
        
        # 최소 차이 갱신
        min_diff = min(min_diff, diff)

    return min_diff

def main():
    N = int(input())  # 사람의 수
    S = [list(map(int, input().split())) for _ in range(N)]  # 능력치

    # 백트래킹을 통한 최소 차이 계산
    result = backtrack(N, S)

    print(result)

if __name__ == "__main__":
    main()
