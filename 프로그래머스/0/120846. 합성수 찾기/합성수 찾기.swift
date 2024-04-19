import Foundation

func solution(_ n:Int) -> Int {
    var cnt: Int = 0
    for i in 1...n {
        var tmp = 0
        for j in 1...i {
            if i % j == 0 {
                tmp += 1
            }
        }
        if tmp >= 3 {
            cnt += 1
        }
    }
    return cnt
}