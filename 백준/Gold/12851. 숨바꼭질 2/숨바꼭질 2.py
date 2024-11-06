from collections import deque

n, k = map(int, input().split())
max_limit = 2 * max(n, k) + 1
arr = [float('inf')] * max_limit 
count = [0] * max_limit 

def bfs(start):
    queue = deque([start])
    arr[start] = 0
    count[start] = 1
    
    while queue:
        tx = queue.popleft()

        for next_pos in (tx - 1, tx + 1, tx * 2):
            if 0 <= next_pos < max_limit:

                if arr[next_pos] > arr[tx] + 1:
                    arr[next_pos] = arr[tx] + 1
                    count[next_pos] = count[tx]
                    queue.append(next_pos)
           
                elif arr[next_pos] == arr[tx] + 1:
                    count[next_pos] += count[tx]

bfs(n)
print(arr[k]) 
print(count[k]) 