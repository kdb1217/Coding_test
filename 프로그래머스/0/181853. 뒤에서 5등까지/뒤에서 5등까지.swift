import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    var inputArr = num_list.sorted()
    let arr = inputArr.prefix(5)
    return Array(arr)
}