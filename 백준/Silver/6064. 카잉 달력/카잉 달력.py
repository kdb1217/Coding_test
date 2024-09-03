def solution(M, N, x, y):

    while x <= M * N:
        if (x - y) % N == 0:  
            print(x)
            return
        x += M 
    print(-1)  

n = int(input())

for i in range(n):
    M, N, x, y = map(int, input().split())
    solution(M, N, x, y)