n = int(input())
arr = list(map(int, input().split()))

start = 0
last = n - 1

result = abs(arr[last] + arr[start])
answer = [arr[start], arr[last]]

while start < last:
    tmp = abs(arr[start] + arr[last])

    if result > tmp:
        result = tmp
        answer = [arr[start], arr[last]]
        
    if arr[start] + arr[last] > 0:
        last -= 1
    elif arr[start] + arr[last] < 0:
        start += 1
    elif arr[start] + arr[last] == 0:
        answer = [arr[start], arr[last]]
        break




print(*sorted(answer))

