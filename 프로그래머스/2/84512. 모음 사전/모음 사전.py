def backtracking(n, lst, arr, word):
    if n == len(word):
        if word not in lst:
            lst.add(word)
        return
    
    for i in range(len(arr)):
        backtracking(n, lst, arr, word + str(arr[i]))

def solution(word):
    arr = ["A","E","I","O","U"]
    alphaSet = set()
    
    
    for i in range(1, 6):
        backtracking(i, alphaSet, arr, "")
    sortedAlpha = sorted(alphaSet)
    
    return (sortedAlpha.index(word) + 1)
