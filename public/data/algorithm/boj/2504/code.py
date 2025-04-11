x = input()  # 입력 문자열
stack = []
result = 0
temp = 1

for i in range(len(x)):
    if x[i] == "(":
        stack.append("(")
        temp *= 2  # 괄호가 열리면 값을 곱함
    elif x[i] == "[":
        stack.append("[")
        temp *= 3
    elif x[i] == ")":
        if not stack or stack[-1] != "(":  # 올바르지 않은 닫힘
            result = 0
            break
        if x[i - 1] == "(":  # 바로 이전에 열린 괄호라면
            result += temp
        stack.pop()
        temp //= 2  # 괄호 닫힘 시 값 나눔
    elif x[i] == "]":
        if not stack or stack[-1] != "[":  # 올바르지 않은 닫힘
            result = 0
            break
        if x[i - 1] == "[":  # 바로 이전에 열린 괄호라면
            result += temp
        stack.pop()
        temp //= 3
    print(x[i], temp, result)
if stack:  # 스택에 남아있으면 잘못된 구조
    result = 0

print(result)
