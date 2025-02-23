# (10 ≤ N ≤ 100,000,000, 1 ≤ K의 원소의 개수 ≤ 3)

n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)

## backtracking을 활용했을때의 사용하는 변수들
answer = ""


# # 완전 탐색
# # 주어진 n을 문자열화 시켜서 값을 비교한다.
# def solution():
#     answer = ""
#     for i in str(n):
#         for j in nums:
#             if str(j) <= i:
#                 answer += str(j)
#                 break
#
#     return answer
#
#
# print(solution())
#

# 재귀(backtracking)

def backtracking(curNum, numArr, targetNum):
    global answer

    if len(curNum) > 0 and int(curNum) > int(targetNum):
        return

    if len(curNum) > 0 and int(targetNum) >= int(curNum):
        if answer == "" or int(curNum) > int(answer):
            answer = curNum

    for i in numArr:
        backtracking(curNum + str(i), numArr, targetNum)


backtracking(answer, nums, str(n))
print(answer)
