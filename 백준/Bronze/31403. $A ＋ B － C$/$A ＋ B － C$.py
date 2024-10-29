# n, k = tuple(map(int, input().split()))
# dptable = [0] * (k + 2)
#
# coin = []
# for i in range(n):
#     coin.append(int(input()))
#
# coin.sort()
#
# for i in coin:
#     dptable[i] = 1
#
# for i in range(k + 1):
#     tmp = []
#     for j in coin:
#         if i - j >= 1:
#             print(tmp)
#             tmp.append(dptable[i - j] + dptable[j])
#
#     dptable[i - j] += min(tmp)
#
# print(dptable)
# print(dptable[k])

a = int(input())
b = int(input())
c = int(input())

print(a + b - c)

stra = str(a)
strb = str(b)
strc = str(c)

print(int(stra + strb) - int(strc))
