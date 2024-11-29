n = int(input())
arr = sorted(map(int, input().split()))
money = int(input())
maxMoney = max(arr)

start = 1
end = maxMoney
if sum(arr) <= money:
    mid = maxMoney
    print(maxMoney)
else:
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in arr:
            if i >= mid:
                cnt += mid
            else:
                cnt += i
        if money - cnt < 0:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid

    print(answer)
