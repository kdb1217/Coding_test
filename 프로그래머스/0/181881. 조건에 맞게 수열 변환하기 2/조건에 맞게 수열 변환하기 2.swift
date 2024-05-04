import Foundation

func solution(_ arr:[Int]) -> Int {
    var answer = arr
    var cnt = 0
    while true {
        var tmp = answer
        for i in 0..<arr.count {
            if answer[i] >= 50 && answer[i] % 2 == 0 {
                tmp[i] /= 2
            } else if answer[i] < 50 && answer[i] % 2 == 1 {
                tmp[i] = tmp[i] * 2 + 1
            }
        }
        if tmp == answer {
            return cnt
        } else {
            answer = tmp
            cnt += 1
        }
    }
}