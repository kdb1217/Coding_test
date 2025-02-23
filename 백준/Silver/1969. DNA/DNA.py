n, m = map(int, input().split())
dnaArr = [input() for _ in range(n)]
hammingDistance = 0
dnaName = ""
dnaInfo = ["A", "C", "G", "T"]

# 각 열을 확인하면서 가장 많이 등장하는 문자 찾기
for i in range(m):
    curDna = ""
    num = n + 1  # 초기값을 n+1로 설정 (최대값으로 시작)

    # 각 문자가 몇 번 등장하는지 체크
    for j in range(4):
        curNum = 0
        for k in range(n):
            if dnaInfo[j] != dnaArr[k][i]:
                curNum += 1
        if curNum < num:  # Hamming 거리 최소값을 찾음
            num = curNum
            curDna = dnaInfo[j]  # 해당 열에서 가장 적합한 문자 선택
    
    # 가장 적합한 문자를 dnaName에 추가
    dnaName += curDna
    hammingDistance += num  # Hamming 거리 누적

# 결과 출력
print(dnaName)
print(hammingDistance)