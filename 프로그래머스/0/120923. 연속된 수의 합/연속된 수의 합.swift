import Foundation

func solution(_ num:Int, _ total:Int) -> [Int] {
    if num == 1 {
        return [total]
    }
    let tmp = Array(1...num - 1).reduce(0, +)
    return Array((total - tmp) / num..<(total - tmp) / num + num)
}