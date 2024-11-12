n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
blocks = []
answer = 0

for i in range(len(arr)):
    if arr[i] > 0:
        blocks.append(i)

if len(blocks) < 2:
    print(answer)
else:
    start = 0
    end = 1
    while start < end < len(blocks):
        h = min(arr[blocks[start]], arr[blocks[end]])

        for i in range(blocks[start], blocks[end]):
            if h - arr[i] < 0:
                continue
            else:
                answer += (h - arr[i])
                arr[i] += (h - arr[i])

        if arr[blocks[start]] >= arr[blocks[end]]:
            end += 1
        else:
            if end - start == 1:
                start += 1
                end += 1
            else:
                start += 1


    print(answer)

