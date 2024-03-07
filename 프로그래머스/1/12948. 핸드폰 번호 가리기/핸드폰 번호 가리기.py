def solution(phone_number):
    arr = list(phone_number)
    for i in range(len(arr) - 4):
        arr[i] = "*"
    answer = "".join(arr)
    return answer