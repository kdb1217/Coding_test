from math import factorial
n, m = map(int, input().split())
total = factorial(n) // (factorial(n-3) * factorial(3))
bad_comb = set()


for i in range(m):
    bad_a, bad_b = map(int, input().split())
    for j in range(1, n+1):
       if j == bad_a or j == bad_b:
           continue
       bad_comb.add(tuple(sorted([bad_a, bad_b, j])))

print(total - len(bad_comb))