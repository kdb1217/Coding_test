def solution(arr):
    if len(arr) == 1:
        arr[0] = -1
        return arr
    else:
        tmp = min(arr)
        arr.remove(tmp)
    answer = arr
    return answer