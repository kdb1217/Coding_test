n = int(input())
answer = 0

cols = [False] * n  
diag1 = [False] * (2 * n - 1)  
diag2 = [False] * (2 * n - 1)  

def backtracking(row):
    global answer

    if row == n:  
        answer += 1
        return

    for col in range(n):
        if not cols[col] and not diag1[row - col + (n - 1)] and not diag2[row + col]:
            cols[col] = diag1[row - col + (n - 1)] = diag2[row + col] = True
            backtracking(row + 1)
            cols[col] = diag1[row - col + (n - 1)] = diag2[row + col] = False  

backtracking(0)
print(answer)