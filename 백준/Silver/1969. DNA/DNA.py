n, m = map(int, input().split())
dnaArr = [input() for _ in range(n)]
hammingDistance = 0
dnaName = ""
dnaInfo = ["A", "C", "G", "T"]

for i in range(m):
    curDna = ""
    num = n + 1
    for j in range(4):
        curNum = 0
        for k in range(n):
            if dnaInfo[j] != dnaArr[k][i]:
                curNum += 1
        if curNum < num:
            num = curNum
            curDna = dnaInfo[j]
    dnaName += curDna
    hammingDistance += num



print(dnaName)
print(hammingDistance)