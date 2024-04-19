import Foundation

func solution(_ numbers:[Int]) -> Int {
    var tmp = numbers.sorted()
    return tmp[0] * tmp[1] > tmp[tmp.count - 1] * tmp[tmp.count - 2] ? tmp[0] * tmp[1] : tmp[tmp.count - 1] * tmp[tmp.count - 2]
}