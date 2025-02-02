n = int(input())
arr = [0]
set1 = set()
set2 = set()
answer = set()

for i in range(n):
    arr.append(int(input()))

visited = [False] * (n + 1)


def dfs(x):
    if not visited[x]:
        set1.add(x)
        set2.add(arr[x])
        visited[x] = True
        dfs(arr[x])


for i in range(1, n + 1):
    dfs(i)
    if set1 == set2:
        answer = answer.union(set1)
    visited = [False] * (n + 1)
    set1 = set()
    set2 = set()



print(len(answer))
arranswer = list(answer)
arranswer.sort()

for i in arranswer:
    print(i)
