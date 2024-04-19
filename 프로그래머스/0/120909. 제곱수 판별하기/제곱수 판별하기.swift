import Foundation

func solution(_ n:Int) -> Int {
    var tmp = Double(n)
    tmp = sqrt(tmp)
    return Int(Int(tmp) * Int(tmp)) == n ? 1 : 2
}