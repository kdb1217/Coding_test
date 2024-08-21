def solution(n):
    tiles = [0] * 600001
    tiles[1] = 1
    tiles[2] = 2
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(3, n + 1):
            tiles[i] = (tiles[i - 1] + tiles[i - 2]) % 1000000007
    return tiles[n]