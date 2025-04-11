n = int(input())
for _ in range(n):
    ans = True
    stack = []
    s = input()
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                ans = False
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                ans = False
                break
    if stack or ans == False:
        print('NO')
    else:
        print('YES')