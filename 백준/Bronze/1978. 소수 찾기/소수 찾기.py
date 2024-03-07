n = int(input())
arr = list(map(int,input().split()))
cnt = 0



def check(num):
    tmp = 2
    if num == 1:
        return False
    
    while (tmp < num):
        if num % tmp == 0:
            return False
        else:
            tmp += 1
    return True

for i in range(len(arr)):
    if check(arr[i]):
        cnt += 1

print(cnt)