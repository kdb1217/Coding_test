n = int(input())

arr = list(map(int, input().split()))
dict = {}
sortedSetArr = sorted(list(set(arr)))

for i in range(len(sortedSetArr)):
    dict[sortedSetArr[i]] = i

for i in range(len(arr)):
    print(dict[arr[i]], end = " ")