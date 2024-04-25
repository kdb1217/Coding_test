import Foundation

func solution(_ arr:[Int]) -> [Int] {
    var nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    var answer = arr
    nums.append(arr.count)
    nums.sort()
    
    for i in arr.count..<nums[nums.firstIndex(of:arr.count)! + 1] {
        answer.append(0)
    }
    return answer
}