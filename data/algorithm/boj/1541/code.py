s = input()
ans = 0
temp = ""
bool = False
for i in s:
    if i == '-' and bool == False:
        temp += i
        temp += '('
        bool = True
    elif i == '-' and bool == True:
        temp += ')'
        temp += i
        bool = False
    else:
        temp += i
if bool == True:
    temp += ')'

print(eval(temp))