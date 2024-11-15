from collections import deque
#풀이게획
#1.소인수분해?
#2.y랑 x를 나누기

def solution(x, y, n):
    answer = 0
    arr = [0] * (y + 1)
    arr[x] = 1
    visited = [False] * (y + 2)
    def bfs(x):
        queue = deque()
        queue.append(x)
        while queue:
            cur = queue.popleft()
            if not cur + n > y and not visited[cur + n]:
                queue.append(cur + n)
                visited[cur + n] = True
                arr[cur + n] = arr[cur] + 1
                
            if not cur * 2 > y and not visited[cur * 2]:
                queue.append(cur * 2)
                visited[cur * 2] = True
                arr[cur * 2] = arr[cur] + 1
                
            if not cur * 3 > y and not visited[cur * 3]:
                queue.append(cur * 3)
                visited[cur * 3] = True
                arr[cur * 3] = arr[cur] + 1
                
        
    bfs(x)
    return -1 if arr[y] == 0 else arr[y] - 1