from collections import deque
n = int(input())

arr = list(map(int, input().split()))
startidx = 0
lastidx = 0
maxFruit = 0
fruits = {}

while lastidx < len(arr):
    if len(fruits.keys()) <= 2:
        if maxFruit < sum(fruits.values()):
            maxFruit = sum(fruits.values())
        if arr[lastidx] in fruits:
            fruits[arr[lastidx]] += 1
        else:
            fruits[arr[lastidx]] = 1
        lastidx += 1

    else:
        fruits[arr[startidx]] -= 1
        if fruits[arr[startidx]] == 0:
            del fruits[arr[startidx]]
        startidx += 1

if len(set(arr[startidx:lastidx])) <= 2:
    if maxFruit < len(arr[startidx:lastidx]):
        maxFruit = len(arr[startidx:lastidx])
print(maxFruit)