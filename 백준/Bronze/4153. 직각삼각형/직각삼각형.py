while(True):
    inputArr = list(map(int, input().split()))
    if inputArr == [0,0,0]:
        break
    inputArr.sort()
    if inputArr[-1] ** 2 == inputArr[0] ** 2 + inputArr[1] ** 2:
        print("right")
    else:
        print("wrong")