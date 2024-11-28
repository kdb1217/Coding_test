n = int(input())
arr = list(map(int, input().split()))
start, end = 0, len(arr) - 1
answer = 0

while start < end:
    answer = max(min(arr[start], arr[end]) * (end - (start - 1) - 2), answer)
    if arr[start] > arr[end]:
        end -= 1
    else:
        start += 1

print(answer)