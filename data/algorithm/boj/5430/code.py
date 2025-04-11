from collections import deque

t = int(input())  # 테스트 케이스 개수

for _ in range(t):
    p = input()  # 수행할 함수
    n = int(input())  # 배열에 들어있는 수의 개수
    arr = input().strip()  # 배열 입력

    # 배열을 파싱하여 정수 리스트로 변환
    if n > 0:
        q = deque(map(int, arr[1:-1].split(",")))
    else:
        q = deque()

    flag = True  # True: 정방향, False: 역방향
    error_occurred = False  # 에러 발생 여부

    # 함수 처리
    for command in p:
        if command == "R":
            flag = not flag  # 뒤집기
        elif command == "D":
            if q:  # 버리기
                if flag:
                    q.popleft()  # 정방향에서 첫 번째 제거
                else:
                    q.pop()  # 역방향에서 첫 번째 제거
            else:
                error_occurred = True
                print("error")
                break

    # 결과 출력
    if not error_occurred:
        if not flag:  # 역방향이면 뒤집기
            q.reverse()
        print(f"[{','.join(map(str, q))}]")
