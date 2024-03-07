n = int(input())
arr = [
    "" for _ in range(n)
]

for i in range(n):
    arr[i] = input()

setArr = set(arr)
arr = list(setArr)
arr.sort()
arr.sort(key = len)
for i in arr:
    print(i)
