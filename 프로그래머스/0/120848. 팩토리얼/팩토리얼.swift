import Foundation

func solution(_ n:Int) -> Int {
    var cnt = 1
    while true {
        if Array(1...cnt).reduce(1, *) > n {
            break
        } else {
            cnt += 1
        }
    }
    return cnt - 1
}