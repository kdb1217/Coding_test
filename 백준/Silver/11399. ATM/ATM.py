n = int(input())
arr = sorted(list(map(int, input().split())))
delayed = 0
answer = 0
# 최소가 되려면 오름차순 정렬이 되어야함

for i in arr:
    answer += delayed + i
    delayed += i

print(answer)
