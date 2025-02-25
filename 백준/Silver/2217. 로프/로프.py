n = int(input())
# W/k 의 최댓값
arr = sorted([int(input()) for _ in range(n)], reverse=True)
answer = 0

for i in range(len(arr)):
    tmpW = (i + 1) * arr[i]

    if tmpW >= answer:
        answer = tmpW

print(answer)

