import Foundation

func solution(_ n:Int) -> [Int] {
    return stride(from: 1, through: n, by: 1).filter{n % $0 == 0}
}