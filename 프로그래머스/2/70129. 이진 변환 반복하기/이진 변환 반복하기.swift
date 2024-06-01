import Foundation

func solution(_ s:String) -> [Int] {
    var removecnt: Int = 0
    var cnt: Int = 0
    var num = s
    while num != "1" {
        removecnt += num.map { String($0) }.filter {$0 == "0"}.count
        num = num.replacingOccurrences(of:"0", with:"")
        cnt += 1
        num = String(num.count, radix:2)
    }
    return [cnt, removecnt]
}