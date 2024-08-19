from collections import deque
n = int(input())

dec = deque()

for i in range(n):
    tmp = input().split(" ")
    if len(tmp) == 2:
        commend = tmp[0]
        num = tmp[1]
    else:
        commend = tmp[0]

    if commend == "push_back":
        dec.append(int(num))
    elif commend == "push_front":
        dec.appendleft(int(num))
    elif commend == "pop_front":
        if not dec:
            print(-1)
        else:
            print(dec.popleft())
    elif commend == "pop_back":
        if not dec:
            print(-1)
        else:
            print(dec.pop())
    elif commend == "size":
        print(len(dec))
    elif commend == "empty":
        if not dec:
            print(1)
        else:
            print(0)
    elif commend == "front":
        if not dec:
            print(-1)
        else:
            print(dec[0])
    else:
        if not dec:
            print(-1)
        else:
            print(dec[-1])




