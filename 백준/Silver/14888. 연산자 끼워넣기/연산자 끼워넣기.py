def solution():
    n = int(input())
    numbers = list(map(int, input().split()))  # 입력받은 숫자 리스트
    operators = list(map(int, input().split()))  # [+, -, *, /] 연산자의 개수
    max_val = -float('inf')
    min_val = float('inf')


    def dfs(depth, current_result, plus, minus, multiply, divide):
        nonlocal max_val, min_val 


        if depth == n:
            max_val = max(max_val, current_result)
            min_val = min(min_val, current_result)
            return

  
        if plus > 0:
            dfs(depth + 1, current_result + numbers[depth], plus - 1, minus, multiply, divide)
        if minus > 0:
            dfs(depth + 1, current_result - numbers[depth], plus, minus - 1, multiply, divide)
        if multiply > 0:
            dfs(depth + 1, current_result * numbers[depth], plus, minus, multiply - 1, divide)
        if divide > 0:
           
            if current_result < 0:
                dfs(depth + 1, -(-current_result // numbers[depth]), plus, minus, multiply, divide - 1)
            else:
                dfs(depth + 1, current_result // numbers[depth], plus, minus, multiply, divide - 1)

    
    dfs(1, numbers[0], operators[0], operators[1], operators[2], operators[3])

    print(max_val)
    print(min_val)

solution()