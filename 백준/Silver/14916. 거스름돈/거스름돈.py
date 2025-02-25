n = int(input())
cnt = 0

while n > 1:
    if n % 5 == 0:
        cnt += n // 5
        n = n % 5
    else:
        n -= 2
        cnt += 1


print(cnt if n == 0 else -1)

