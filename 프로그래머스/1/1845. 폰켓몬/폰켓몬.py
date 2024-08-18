
def solution(nums):
    setArr = list(set(nums))
    dict = {}
    for i in range(len(setArr)):
        dict[setArr[i]] = nums.count(setArr[i])
        
    
    if len(dict) >= len(nums) / 2:
        return len(nums) // 2
    else:
        return len(dict)


