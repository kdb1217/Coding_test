"""
스타트와 링크
백트래킹!
"""

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 200 * 11


def cal(teama, teamb):
    suma, sumb = 0, 0
    for i in range(len(teama)):
        for j in range(len(teama)):
            suma += arr[teama[i]][teama[j]]
            sumb += arr[teamb[i]][teamb[j]]

    return abs(suma - sumb)


def dfs(n, teama, teamb):
    global ans
    tmp = 0
    if n == N:
        if len(teama) == len(teamb):
            ans = min(ans, cal(teama, teamb))
        return

    dfs(n + 1, teama + [n], teamb)
    dfs(n + 1, teama, teamb + [n])


dfs(0, [], [])
print(ans)
