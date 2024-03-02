inputNum = int(input())
inputString = input()
answer = 0
for i in range(inputNum):
    answer += (ord(inputString[i]) - 96) * (31 ** i)


print(answer)