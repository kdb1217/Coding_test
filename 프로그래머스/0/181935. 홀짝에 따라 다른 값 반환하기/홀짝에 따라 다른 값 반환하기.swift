import Foundation

func solution(_ n:Int) -> Int {
    let oddSum1 = Array(1...n).filter { $0 % 2 == 1 }.reduce(0, +)
    let evenSum1 = Array(1...n).filter { $0 % 2 == 0 }.map { $0 * $0 }.reduce(0, +)
    return n % 2 == 1 ? oddSum1 : evenSum1
}