n = int(input())
arr = list(map(int,input().split()))
m = int(input())
arr1 = list(map(int,input().split()))
temp = list(set(arr + arr1))

for i in range(len(temp)):
    if temp[i] != 0:
        
        for j in range(i+1,len(temp)):
            print(i,j,temp)
            if temp[j] % temp[i] == 0:
                temp[j] = 0
        print(temp)