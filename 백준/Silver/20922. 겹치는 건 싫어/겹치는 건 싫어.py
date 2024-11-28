n, k = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
answer = end - (start - 1)
numDict = dict()

for i in range(len(arr)):
    if arr[i] in numDict:
        numDict[arr[i]] += 1
        if numDict[arr[i]] > k:
            while numDict[arr[i]] > k:
                numDict[arr[start]] -= 1
                if numDict[arr[start]] == 0:
                    del numDict[arr[start]]
                start += 1
    else:
        numDict[arr[i]] = 1

    answer = max(answer, (i - (start - 1)))



print(answer)
